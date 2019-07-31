# encoding:utf-8

import random, time, Queue
from multiprocessing.managers import BaseManager


# 使用标准函数来代替lambda函数，避免python2.7中，pickle无法序列化lambda的问题
def get_task_queue():
    global task_queue
    return task_queue

# 使用标准函数来代替lambda函数，避免python2.7中，pickle无法序列化lambda的问题
def get_result_queue():
    global task_queue
    return result_queue

def startManager(host, port, authkey):
    # 把两个Queue都注册到网络上，callable参数关联了Queue对象，注意回调函数不能使用括号
    BaseManager.register('get_task_queue', callable=get_task_queue)
    BaseManager.register('get_result_queue', callable=get_result_queue)
    # 设置host,绑定端口port，设置验证码为authkey
    manager = BaseManager(address=(host, port), authkey=authkey)
    # 启动manager服务器
    manager.start()
    return manager

def put_queue(manager):
    # 通过网络访问queueu
    task = manager.get_task_queue()
    for i in range(10):
        n = random.randint(0, 1000)
        #n = raw_input("input:")
        task.put(n)
        print 'Put task :',n
        time.sleep(0.1)

def get_result(manager):
    #通过网络获取result_queue
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    while 1:
        n = result.get()
        time.sleep(0.000001)
        print n
        if result.empty() and task.empty():
            result.put('end')
            time.sleep(1)
            break

if __name__ == "__main__":
    # 发送任务的队列
    task_queue = Queue.Queue()
    # 接收结果的队列
    result_queue = Queue.Queue()
    host = '127.0.0.1'
    port = 5000
    authkey = 'abc'
    # 启动manager服务器
    manager = startManager(host, port, authkey)
    # 给task队列添加数据
    put_queue(manager)

    get_result(manager)
    # 关闭服务器
    manager.shutdown()
'''
    while True:
      if task_queue.empty() and result_queue.empty():
        time.sleep(10)
        print 'queue is empty'
        manager.shutdown()
        break
      else:
        print task_queue.empty(),result_queue.empty()
        sleep(1)
        '''