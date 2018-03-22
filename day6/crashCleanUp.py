#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tkinter
import tkinter.messagebox, tkinter.simpledialog
import os, os.path
import threading

rubbishEXT = ['.tmp', '.bak','.old', '.wbk', '.xlk', '._mp', '.gid', '.chk', '.syd', '.$$$', '.@@@', '.~*']


def GetDrives():
        drives = []
        for i in range(65, 91):
                vol = chr(i) + ':/'
                if os.path.isdir(vol):
                        drives.append(vol)
        return tuple(drives)


class Window:
        def __init__(self):
                self.root = tkinter.Tk()
                # 创建菜单
                menu = tkinter.Menu(self.root)

                # 创建“系统”子菜单
                submenu = tkinter.Menu(menu, tearoff=0)
                submenu.add_command(label='关于...', command=self.MenuAbout)
                submenu.add_separator()
                submenu.add_command(label='退出', command=self.MenuExit)
                menu.add_cascade(label='系统', menu=submenu)
                # 创建“清理”子菜单
                submenu = tkinter.Menu(menu, tearoff=0)
                submenu.add_command(label="扫描垃圾文件", command=self.MenuScanRubbish)
                submenu.add_command(label="删除垃圾文件", command=self.MenuDelRubbish)
                menu.add_cascade(label="清理", menu=submenu)

                # 创建查找子菜单
                submenu = tkinter.Menu(menu, tearoff=0)
                submenu.add_command(label="搜索大文件", command=self.MenuScanBigFile)
                submenu.add_separator()
                submenu.add_command(label="按名称搜索文件", command=self.MenuSearchFile)
                menu.add_cascade(label="搜索", menu=submenu)

                self.root.config(menu=menu)

                # 创建标签,用于显示状态信息
                self.progress = tkinter.Label(self.root, anchor=tkinter.W, text="状态", bitmap='hourglass',
                                              compound='left')
                self.progress.place(x=10, y=370, width=480, height=20)

                # 创建文本框,显示文件列表
                self.flist = tkinter.Text(self.root)
                self.flist.place(x=10, y=10, width=480, height=350)

                # 为文本框添加垂直滚动条
                self.vscroll = tkinter.Scrollbar(self.flist)
                self.vscroll.pack(side='right', fill='y')
                self.flist['yscrollcommand'] = self.vscroll.set
                self.vscroll['command'] = self.flist.yview

        def MenuAbout(self):
                tkinter.messagebox.showinfo('Crash_Cleaner', '本软件版权归：StaryJie所有,欢迎使用!')

        def MenuExit(self):
                self.root.quit()

        def MenuScanRubbish(self):
                result = tkinter.messagebox.askquestion('Crash_Cleaner', '扫描垃圾文件需较长时间,是否继续?')
                if result == 'no':
                        return
                tkinter.messagebox.showinfo('Crash_Cleaner', '马上开始扫描垃圾文件!')
                # self.ScanRubbish()
                self.drives = GetDrives()
                t = threading.Thread(target=self.ScanRubbish, args=(self.drives,))  # 创建线程
                t.start()  # 开始线程

        def MenuDelRubbish(self):
                result = tkinter.messagebox.askquestion('Crash_Cleaner', '删除垃圾文件时间较长,是否继续?')
                if result == 'no':
                        return
                tkinter.messagebox.showinfo('Crash_Cleaner', '马上开始删除垃圾文件!')
                self.drives = GetDrives()
                t = threading.Thread(target=self.DeleteRubbish, args=(self.drives,))
                t.start()

        def MenuScanBigFile(self):
                s = tkinter.simpledialog.askinteger('Crash_Cleaner', '请设置文件大小(M)')
                t = threading.Thread(target=self.ScanBigFile, args=(s,))
                t.start()

        def MenuSearchFile(self):
                s = tkinter.simpledialog.askstring('Crash_Cleaner', '请输入文件名的部分字符')
                t = threading.Thread(target=self.SearchFile, args=(s,))
                t.start()

        def ScanRubbish(self, scanpath):
                global rubbishEXT
                total = 0
                filesize = 0
                for drive in scanpath:
                        for root, dirs, files in os.walk(drive):
                                try:
                                        for file in files:
                                                filesplit = os.path.splitext(file)
                                                if filesplit[1] == "":  # 若文件无扩展名
                                                        continue
                                                try:
                                                        if rubbishEXT.index(filesplit[1]) >= 0:  # 扩展名在列表中
                                                                fname = os.path.join(os.path.abspath(root), file)
                                                                filesize += os.path.getsize(fname)
                                                                if total % 15 == 0:
                                                                        self.flist.delete(0.0, tkinter.END)
                                                                        # self.flist.insert(tkinter.END, fname + '\n')
                                                                l = len(fname)
                                                                if l > 50:
                                                                        self.progress['text'] = fname[
                                                                                                :25] + '...' + fname[
                                                                                                               l - 25:l]
                                                                self.flist.insert(tkinter.END, fname + '\n')
                                                                self.progress['text'] = fname
                                                                total += 1  # 计数
                                                except ValueError:
                                                        pass
                                except Exception as e:
                                        print(e)
                                        pass
                self.progress['text'] = '找到 %s 个垃圾文件,共占用 %.2f M磁盘空间' % (total, filesize / 1024 / 1024)

        def DeleteRubbish(self, scanpath):
                global rubbishEXT
                total = 0
                filesize = 0
                for drive in scanpath:
                        for root, dirs, files in os.walk(drive):
                                try:
                                        for file in files:
                                                filesplit = os.path.splitext(file)
                                                if filesplit[1] == "":  # 若文件无扩展名
                                                        continue
                                                try:
                                                        if rubbishEXT.index(filesplit[1]) >= 0:  # 扩展名在列表中
                                                                fname = os.path.join(os.path.abspath(root), file)
                                                                filesize += os.path.getsize(fname)
                                                                try:
                                                                        os.remove(fname)  # 删除文件
                                                                        # self.flist.insert(tkinter.END, fname + '\n')
                                                                        l = len(fname)
                                                                        if l > 50:
                                                                                self.progress['text'] = fname[
                                                                                                        :25] + '...' + fname[
                                                                                                                       l - 25:l]
                                                                        if total % 15 == 0:
                                                                                self.flist.delete(0.0, tkinter.END)
                                                                        self.flist.insert(tkinter.END,
                                                                                          'Deleted' + fname + '\n')
                                                                        self.progress['text'] = fname
                                                                        total += 1  # 计数
                                                                except:  # 不能删除,跳过
                                                                        pass
                                                except ValueError:
                                                        pass
                                except Exception as e:
                                        print(e)
                                        pass
                self.progress['text'] = '删除 %s 个垃圾文件,收回 %.2f M磁盘空间' % (total, filesize / 1024 / 1024)

        def ScanBigFile(self, filesize):
                total = 0
                filesize = filesize * 1024 * 1024
                for drive in GetDrives():
                        for root, dirs, files in os.walk(drive):
                                for file in files:
                                        try:
                                                fname = os.path.abspath(os.path.join(root, file))
                                                fsize = os.path.getsize(fname)
                                                self.progress['text'] = fname
                                                if fsize >= filesize:
                                                        total += 1
                                                        self.flist.insert(tkinter.END, '%s, [%.2f M]\n' % (
                                                        fname, fsize / 1024 / 1024))
                                        except:
                                                pass
                self.progress['text'] = '找到%s个超过 %s M的大文件' % (total, filesize / 1024 / 1024)

        def SearchFile(self, fname):
                total = 0
                fname = fname.upper()
                for drive in GetDrives():
                        for root, dirs, files in os.walk(drive):
                                for file in files:
                                        try:
                                                fn = os.path.abspath(os.path.join(root, file))
                                                l = len(fn)
                                                if l > 50:
                                                        self.progress['text'] = fn[:25] + '...' + fn[l - 25:l]
                                                else:
                                                        self.progress['text'] = fn
                                                if file.upper().find(fname) >= 0:
                                                        total += 1
                                                        self.flist.insert(tkinter.END, fn + '\n')
                                        except:
                                                pass
                self.progress['text'] = '找到 %s 个文件' % (total)

        def mainloop(self):
                self.root.title("Crash_Cleaner")
                self.root.minsize(500, 400)
                self.root.maxsize(500, 400)
                self.root.mainloop()


if __name__ == "__main__":
        window = Window()
        window.mainloop()