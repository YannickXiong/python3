# -*- coding: utf-8 -*-
# @Time    : 2017/12/29 19:47
# @Author  : Yannick
# @File    : adbmgr.py


import subprocess


class Shell:

    def __init__(self):
        self.stdin = subprocess.PIPE
        self.stdout = subprocess.PIPE
        self.stderr = subprocess.PIPE
        self.shell = True
        self.universal_newlines = True

    def invoke(self, command):
        # out, err = subprocess.Popen(command,
        #                             stdin=self.stdin,
        #                             stdout=self.stdout,
        #                             stderr=self.stderr,
        #                             shell=self.shell,
        #                             universal_newlines=self.universal_newlines)
        # return out, err
        print("invoke::", self.shell)
        print("invoke::", command)


shell = Shell()






class AdbMgr:

    def __init__(self):
        self.device_id = "emulator-5556"
        self.adb_bin = "adb -s"
        self.noshell = False
        self.shell = True

    def args_wrapper(self, func):
        def _wrapper(*args, **kwargs):
            print("_wrapper:: args => %s, kwargs => %s" % (args, kwargs))
            if kwargs["shell"]:
                args = "%s %s shell %s " % (self.adb_bin, self.device_id, *args)
            else:
                args = "%s %s %s " % (self.adb_bin, self.device_id, *args)

            ret = func(args)

            return ret

        return _wrapper

    def execute(self, *args, **kwargs):
        return self.args_wrapper(shell.invoke)(*args, **kwargs)

    def get_state(self):
        self.execute("get-state", shell=self.noshell)


    def get_serialno(self):
        self.execute("get-serialno", shell=self.shell)




if __name__ == "__main__":
    adbmgr = AdbMgr()
    adbmgr.get_state()
    adbmgr.get_serialno()

