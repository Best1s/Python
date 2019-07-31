# -*- coding: utf-8 -*-
def break_words(stuff):
  ''' This function will break up words for us. '''
  words = stuff.split(' ')  #以空格分割字符串
  return words
def sort_words(words):
  """Sorts the words."""
  return sorted(words)  #排序
def print_first_word(words):
  """Prints the first word after popping it off."""
  word = words.pop(0)   #赋值并删除
  print word
def print_last_word(words):
  """Prints the last word after popping it off."""
  word = words.pop(-1)  #赋值并删除最后一个
  print word
def sort_sentence(sentence):
  """Takes in a full sentence and returns the sorted words."""
  words = break_words(sentence)   #调用break_words函数分割
  return sort_words(words)  #调用sort_words函数排序
def print_first_and_last(sentence):
  """Prints the first and last words of the sentence."""
  words = break_words(sentence)
  print_first_word(words)
  print_last_word(words)
def print_first_and_last_sorted(sentence):
  """Sorts the words then prints the first and last one."""
  words = sort_sentence(sentence)
  print_first_word(words)
  print_last_word(words)