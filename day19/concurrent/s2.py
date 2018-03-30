#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import socketserver

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        # print(self.request,self.client_address,self.server)
        conn = self.request
        conn.sendall(bytes('欢迎致电10001，请输入1获取指令帮助,0转人工服务.',encoding="utf-8"))
        Flag = True
        msg = '''
        尊敬的用户：您可回复【】内指令查询信息：
        【108】流量/时长查询
        【193】套餐余量查询
        【101】当月话费查询
        【102】帐户余额查询
        【103】上月账单查询
        【104】历史账单查询
        【105】积分查询
        【106】积分兑换话费
        【110】缴费记录查询
        【111】欠费查询
        【701】话费充值（充值卡）
        【777】话费充值（银行卡）
        【457】流量包
        【34】免费换4G卡
        话费详单查询请登录欢GO网站或欢GO客户端。
        如需人工服务请编辑事件内容至10001000，或详询10000号。
        回复4576720办理20元2GB流量7天包，回复4576105办理5元1GB流量1天包，流量使用详情可回复108查询。
        '''
        while Flag:
            data_bytes = conn.recv(1024)
            data = str(data_bytes,encoding="utf-8")
            if data == 'exit':
                Flag = False
            elif data == '0':
                conn.sendall(bytes('通话可能会被录音.balabala一大推',encoding="utf-8"))
            elif data == '1':
                conn.sendall(bytes(msg,encoding="utf-8"))
            elif data == '108':
                conn.sendall(bytes('正在为您查询，请稍等...',encoding="utf-8"))
            elif data == '193':
                conn.sendall(bytes('正在为您查询，请稍等...',encoding="utf-8"))
            elif data == '101':
                conn.sendall(bytes('正在为您查询，请稍等...',encoding="utf-8"))
            elif data == '102':
                conn.sendall(bytes('正在为您查询，请稍等...',encoding="utf-8"))
            elif data == '103':
                conn.sendall(bytes('正在为您查询，请稍等...',encoding="utf-8"))
            elif data == '104':
                conn.sendall(bytes('正在为您查询，请稍等...',encoding="utf-8"))
            elif data == '105':
                conn.sendall(bytes('正在为您查询，请稍等...',encoding="utf-8"))
            elif data == '106':
                conn.sendall(bytes('正在为您查询，请稍等...',encoding="utf-8"))
            elif data == '110':
                conn.sendall(bytes('正在为您查询，请稍等...',encoding="utf-8"))
            elif data == '111':
                conn.sendall(bytes('正在为您查询，请稍等...',encoding="utf-8"))
            elif data == '701':
                conn.sendall(bytes('正在为您查询，请稍等...',encoding="utf-8"))
            elif data == '777':
                conn.sendall(bytes('正在为您查询，请稍等...',encoding="utf-8"))
            elif data == '457':
                conn.sendall(bytes('正在为您查询，请稍等...',encoding="utf-8"))
            elif data == '34':
                conn.sendall(bytes('正在为您查询，请稍等...',encoding="utf-8"))
            else:
                conn.sendall(bytes('没有该指令，请重新输入.',encoding="utf-8"))



if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(("127.0.0.1",9000),MyServer)
    server.serve_forever()