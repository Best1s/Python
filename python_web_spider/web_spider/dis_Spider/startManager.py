import Queue
from NodeManager import NodeManager
from multiprocessing import Process
if __name__ == '__main__':

  url_q = Queue.Queue()
  result_q = Queue.Queue()
  store_q = Queue.Queue()
  conn_q = Queue.Queue()

  node = NodeManager()
  manager = node.start_Manager(url_q,result_q)
  
  url_manager_proc = Process(target=node.url_manager_proc,args=(url_q,conn_q,'http://baike.baidu.com/view/284853.html'))
  
  result_solve_proc = Process(target=node.result_solve_proc,args=(result_q,conn_q,store_q))
  store_proc = Process(target=node.store_proc,args=(store_q,))

  url_manager_proc.start()
  result_solve_proc.start()
  store_proc.start()
  manager.get_server().serve_forever()
  '''
  node.url_manager_proc(url_q,conn_q,'http://baike.baidu.com/view/284853.html')
  node.result_solve_proc(result_q,conn_q,store_q)
  node.store_proc(store_q)
  manager.get_server().serve_forever()
  '''