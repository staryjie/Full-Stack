## socketserver实现高并发操作

### SocketServer模块

SocketServer内部使用 IO多路复用 以及 “多线程” 和 “多进程” ，从而实现并发处理多个客户端请求的Socket服务端。即：每个客户端请求连接到服务器时，Socket服务端都会在服务器是创建一个“线程”或者“进程” 专门负责处理当前客户端的所有请求。

![](https://images2015.cnblogs.com/blog/425762/201512/425762-20151226114322968-1230975336.jpg)

#### ThreadingTCPServer

ThreadingTCPServer实现的Soket服务器内部会为每个client创建一个<font color="red">`线程`</font>，该线程用来和客户端进行交互。

1、ThreadingTCPServer基础

使用ThreadingTCPServer:

* 创建一个继承自 SocketServer.BaseRequestHandler 的类
* 类中必须定义一个名称为 handle 的方法
* 启动ThreadingTCPServer

socketserver实现服务端：

```python
#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import socketserver

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        # print self.request,self.client_address,self.server
        conn = self.request
        conn.sendall(bytes('欢迎致电 10086，请输入1xxx,0转人工服务.',encoding="utf-8"))
        Flag = True
        while Flag:
            data_bytes = conn.recv(1024)
            data = str(data_bytes,encoding="utf-8")
            if data == 'exit':
                Flag = False
            elif data == '0':
                conn.sendall(bytes('通过可能会被录音.balabala一大推',encoding="utf-8"))
            elif data == '1':
                conn.sendall(bytes('回复“11”,查询实时话费',encoding="utf-8"))
            elif data == '11':
                conn.sendall(bytes('自2018年03月01日到目前为止，您的话费余额为1989.65元。感谢您的使用！',encoding="utf-8"))
            else:
                conn.sendall('请重新输入.')


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),MyServer)
    server.serve_forever()
```

socketserver实现客户端：


```python
#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import socket

ip_port = ('127.0.0.1',9000)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)

while True:
    data_bytes = sk.recv(1024)
    data_str = str(data_bytes,encoding="utf-8")
    print('receive:',data_str)
    inp = input('please input:')
    sk.sendall(bytes(inp,encoding="utf-8"))
    if inp == 'exit':
        break

sk.close()
```

2、ThreadingTCPServer源码剖析

ThreadingTCPServer的类图关系如下：

![](https://images2015.cnblogs.com/blog/425762/201512/425762-20151226133025359-790393993.jpg)

内部调用流程为：

1. 启动服务端程序
2. 执行 TCPServer.__init__ 方法，创建服务端Socket对象并绑定 IP 和 端口
3. 执行 BaseServer.__init__ 方法，将自定义的继承自SocketServer.BaseRequestHandler 的类 MyRequestHandle赋值给 <font color="red">self.RequestHandlerClass</font>
4. 执行 BaseServer.server_forever 方法，While 循环一直监听是否有客户端请求到达 ...
5. 当客户端连接到达服务器
6. 执行 ThreadingMixIn.process_request 方法，创建一个 “线程” 用来处理请求
7. 执行 ThreadingMixIn.process_request_thread方法
8. 执行 BaseServer.finish_request 方法，执行 <font color="red">self.RequestHandlerClass()</font>即：执行自定义 MyRequestHandler 的构造方法（自动调用基类BaseRequestHandler的构造方法，在该构造方法中又会调用 MyRequestHandler的handle方法）

ThreadingTCPServer相关源码：

BaseServer源码：


```python
class BaseServer:

    """Base class for server classes.

    Methods for the caller:

    - __init__(server_address, RequestHandlerClass)
    - serve_forever(poll_interval=0.5)
    - shutdown()
    - handle_request()  # if you do not use serve_forever()
    - fileno() -> int   # for select()

    Methods that may be overridden:

    - server_bind()
    - server_activate()
    - get_request() -> request, client_address
    - handle_timeout()
    - verify_request(request, client_address)
    - server_close()
    - process_request(request, client_address)
    - shutdown_request(request)
    - close_request(request)
    - handle_error()

    Methods for derived classes:

    - finish_request(request, client_address)

    Class variables that may be overridden by derived classes or
    instances:

    - timeout
    - address_family
    - socket_type
    - allow_reuse_address

    Instance variables:

    - RequestHandlerClass
    - socket

    """

    timeout = None

    def __init__(self, server_address, RequestHandlerClass):
        """Constructor.  May be extended, do not override."""
        self.server_address = server_address
        self.RequestHandlerClass = RequestHandlerClass
        self.__is_shut_down = threading.Event()
        self.__shutdown_request = False

    def server_activate(self):
        """Called by constructor to activate the server.

        May be overridden.

        """
        pass

    def serve_forever(self, poll_interval=0.5):
        """Handle one request at a time until shutdown.

        Polls for shutdown every poll_interval seconds. Ignores
        self.timeout. If you need to do periodic tasks, do them in
        another thread.
        """
        self.__is_shut_down.clear()
        try:
            while not self.__shutdown_request:
                # XXX: Consider using another file descriptor or
                # connecting to the socket to wake this up instead of
                # polling. Polling reduces our responsiveness to a
                # shutdown request and wastes cpu at all other times.
                r, w, e = _eintr_retry(select.select, [self], [], [],
                                       poll_interval)
                if self in r:
                    self._handle_request_noblock()
        finally:
            self.__shutdown_request = False
            self.__is_shut_down.set()

    def shutdown(self):
        """Stops the serve_forever loop.

        Blocks until the loop has finished. This must be called while
        serve_forever() is running in another thread, or it will
        deadlock.
        """
        self.__shutdown_request = True
        self.__is_shut_down.wait()

    # The distinction between handling, getting, processing and
    # finishing a request is fairly arbitrary.  Remember:
    #
    # - handle_request() is the top-level call.  It calls
    #   select, get_request(), verify_request() and process_request()
    # - get_request() is different for stream or datagram sockets
    # - process_request() is the place that may fork a new process
    #   or create a new thread to finish the request
    # - finish_request() instantiates the request handler class;
    #   this constructor will handle the request all by itself

    def handle_request(self):
        """Handle one request, possibly blocking.

        Respects self.timeout.
        """
        # Support people who used socket.settimeout() to escape
        # handle_request before self.timeout was available.
        timeout = self.socket.gettimeout()
        if timeout is None:
            timeout = self.timeout
        elif self.timeout is not None:
            timeout = min(timeout, self.timeout)
        fd_sets = _eintr_retry(select.select, [self], [], [], timeout)
        if not fd_sets[0]:
            self.handle_timeout()
            return
        self._handle_request_noblock()

    def _handle_request_noblock(self):
        """Handle one request, without blocking.

        I assume that select.select has returned that the socket is
        readable before this function was called, so there should be
        no risk of blocking in get_request().
        """
        try:
            request, client_address = self.get_request()
        except socket.error:
            return
        if self.verify_request(request, client_address):
            try:
                self.process_request(request, client_address)
            except:
                self.handle_error(request, client_address)
                self.shutdown_request(request)

    def handle_timeout(self):
        """Called if no new request arrives within self.timeout.

        Overridden by ForkingMixIn.
        """
        pass

    def verify_request(self, request, client_address):
        """Verify the request.  May be overridden.

        Return True if we should proceed with this request.

        """
        return True

    def process_request(self, request, client_address):
        """Call finish_request.

        Overridden by ForkingMixIn and ThreadingMixIn.

        """
        self.finish_request(request, client_address)
        self.shutdown_request(request)

    def server_close(self):
        """Called to clean-up the server.

        May be overridden.

        """
        pass

    def finish_request(self, request, client_address):
        """Finish one request by instantiating RequestHandlerClass."""
        self.RequestHandlerClass(request, client_address, self)

    def shutdown_request(self, request):
        """Called to shutdown and close an individual request."""
        self.close_request(request)

    def close_request(self, request):
        """Called to clean up an individual request."""
        pass

    def handle_error(self, request, client_address):
        """Handle an error gracefully.  May be overridden.

        The default is to print a traceback and continue.

        """
        print '-'*40
        print 'Exception happened during processing of request from',
        print client_address
        import traceback
        traceback.print_exc() # XXX But this goes to stderr!
        print '-'*40
```

TCPServer源码：


```python
class TCPServer(BaseServer):

    """Base class for various socket-based server classes.

    Defaults to synchronous IP stream (i.e., TCP).

    Methods for the caller:

    - __init__(server_address, RequestHandlerClass, bind_and_activate=True)
    - serve_forever(poll_interval=0.5)
    - shutdown()
    - handle_request()  # if you don't use serve_forever()
    - fileno() -> int   # for select()

    Methods that may be overridden:

    - server_bind()
    - server_activate()
    - get_request() -> request, client_address
    - handle_timeout()
    - verify_request(request, client_address)
    - process_request(request, client_address)
    - shutdown_request(request)
    - close_request(request)
    - handle_error()

    Methods for derived classes:

    - finish_request(request, client_address)

    Class variables that may be overridden by derived classes or
    instances:

    - timeout
    - address_family
    - socket_type
    - request_queue_size (only for stream sockets)
    - allow_reuse_address

    Instance variables:

    - server_address
    - RequestHandlerClass
    - socket

    """

    address_family = socket.AF_INET

    socket_type = socket.SOCK_STREAM

    request_queue_size = 5

    allow_reuse_address = False

    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
        """Constructor.  May be extended, do not override."""
        BaseServer.__init__(self, server_address, RequestHandlerClass)
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)
        if bind_and_activate:
            try:
                self.server_bind()
                self.server_activate()
            except:
                self.server_close()
                raise

    def server_bind(self):
        """Called by constructor to bind the socket.

        May be overridden.

        """
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()

    def server_activate(self):
        """Called by constructor to activate the server.

        May be overridden.

        """
        self.socket.listen(self.request_queue_size)

    def server_close(self):
        """Called to clean-up the server.

        May be overridden.

        """
        self.socket.close()

    def fileno(self):
        """Return socket file number.

        Interface required by select().

        """
        return self.socket.fileno()

    def get_request(self):
        """Get the request and client address from the socket.

        May be overridden.

        """
        return self.socket.accept()

    def shutdown_request(self, request):
        """Called to shutdown and close an individual request."""
        try:
            #explicitly shutdown.  socket.close() merely releases
            #the socket and waits for GC to perform the actual close.
            request.shutdown(socket.SHUT_WR)
        except socket.error:
            pass #some platforms may raise ENOTCONN here
        self.close_request(request)

    def close_request(self, request):
        """Called to clean up an individual request."""
        request.close()
```

ThreadingMixIn源码：

```python
class ThreadingMixIn:
    """Mix-in class to handle each request in a new thread."""

    # Decides how threads will act upon termination of the
    # main process
    daemon_threads = False

    def process_request_thread(self, request, client_address):
        """Same as in BaseServer but as a thread.

        In addition, exception handling is done here.

        """
        try:
            self.finish_request(request, client_address)
            self.shutdown_request(request)
        except:
            self.handle_error(request, client_address)
            self.shutdown_request(request)

    def process_request(self, request, client_address):
        """Start a new thread to process the request."""
        t = threading.Thread(target = self.process_request_thread,
                             args = (request, client_address))
        t.daemon = self.daemon_threads
        t.start()
```

ThreadingTCPServer源码：

```python
class ThreadingTCPServer(ThreadingMixIn, TCPServer): pass
```

RequestHandler相关源码：


```python
class BaseRequestHandler:

    """Base class for request handler classes.

    This class is instantiated for each request to be handled.  The
    constructor sets the instance variables request, client_address
    and server, and then calls the handle() method.  To implement a
    specific service, all you need to do is to derive a class which
    defines a handle() method.

    The handle() method can find the request as self.request, the
    client address as self.client_address, and the server (in case it
    needs access to per-server information) as self.server.  Since a
    separate instance is created for each request, the handle() method
    can define arbitrary other instance variariables.

    """

    def __init__(self, request, client_address, server):
        self.request = request
        self.client_address = client_address
        self.server = server
        self.setup()
        try:
            self.handle()
        finally:
            self.finish()

    def setup(self):
        pass

    def handle(self):
        pass

    def finish(self):
        pass
```


