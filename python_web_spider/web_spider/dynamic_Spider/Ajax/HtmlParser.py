#coding: utf-8
import re
import json

class HtmlParser(object):
  def parser_url(self,page_url,response):
    pattern = re.compile(r'(http://movie.mtime.com/(\d+)/)')
    urls = pattern.findall(response)
    
    if urls != None:
      #将urls进行去重
      return list(set(urls))
    else:
      return None

  def parser_json(self,page_url,response):
    '''
    解析响应
    ：param response
    : return:
    '''
    #将 ‘=’ 和 ‘；’ 之间的内容提取出来
    pattern = re.compile(r'=(.*?);')
    result = pattern.findall(response)[0]
    if result != None:
      # json 模块加载字符串
      value = json.loads(result)
      value = value.get("value") #add
      try:
        #isRelease = value.get('value').get('isRelease')
        isRelease = value.get('isRelease')
      except Exception,e:
        print e
        return None
      if isRelease:
        if value.get('value').get('hotValue') == None:
          return self._parser_release(page_url,value)
        else:
          return self._parser_no_release(page_url,value,isRelease=2)
      else:
        return self._parser_no_release(self,page_url,value)
  def _parser_release(self,page_url,value):
    '''
    解析已经上映的信息
    :param page_url:电影链接
    :param value:json 数据
    :return
    '''
    try:
      isRelease = 1
      #movieRating = value.get('value').get('movieRating')
      #boxOffice = value.get('value').get('boxOffice')
      #movieTitle = value.get('value').get('movieTitle')

      movieRating = value.get('movieRating')
      boxOffice = value.get('boxOffice')
      movieTitle = value.get('movieTitle')

      RPictureFinal = movieRating.get('RPictureFinal')
      RStoryFinal = movieRating.get('RStoryFinal')
      RDirectorFinal = movieRating.get('RDirectorFinal')
      ROtherFinal = movieRating.get('ROtherFinal')
      RatingFinal = movieRating.get('RatingFinal')

      MovieId = movieRating.get('MovieId')
      Usercount = movieRating.get('Usercount')
      AttitudeCount = movieRating.get('AttitudeCount')

      TotalBoxOffice = boxOffice.get('TotalBoxOffice')
      TotalBoxOfficeUnit = boxOffice.get('TotalBoxOfficeUnit')
      TodayBoxOffice1 = boxOffice.get('TodayBoxOffice1')
      TotalBoxOfficeUnit1 = boxOffice.get('TotalBoxOfficeUnit')

      ShowDays = boxOffice.get('ShowDays')
      try:
        Rank = boxOffice.get('Rank')
      except Exception,e:
        Rank = 0
      return (MovieId,movieTitle,RatingFinal,ROtherFinal,RPictureFinal,RDirectorFinal,
        RStoryFinal,Usercount,AttitudeCount,TotalBoxOffice + TotalBoxOfficeUnit,
        TotalBoxOffice1 + TotalBoxOfficeUnit1,Rank,ShowDays,isRelease)
    except Exception,e:
      print
      print "error",e,page_url,value
      return None
    
  def _parser_no_release(self,page_url,value,isRelease = 0):
    '''
    解析未上映的信息
    :param page_url:电影链接
    :param value:json 数据
    :return
    '''
    try:
      #movieRating = value.get('value').get('movieRating')
      #movieTitle = value.get('value').get('movieTitle')
      
      movieRating = value.get('movieRating')
      movieTitle = value.get('movieTitle')
      
      RPictureFinal = movieRating.get('RPictureFinal')
      RStoryFinal = movieRating.get('RStoryFinal')
      RDirectorFinal = movieRating.get('RDirectorFinal')
      ROtherFinal = movieRating.get('ROtherFinal')
      RatingFinal = movieRating.get('RatingFinal')

      MovieId = movieRating.get('MovieId')
      Usercount = movieRating.get('Usercount')
      AttitudeCount = movieRating.get('AttitudeCount')

      try:
        Rank = value.get('hotValue').get('Ranking')
      except Exception,e:
        Rank = 0
      return (MovieId,movieTitle,RatingFinal,
        ROtherFinal,RPictureFinal,RDirectorFinal,
        RStoryFinal,Usercount,AttitudeCount,u'无',
        u'无',
        Rank,0,isRelease)
    except Exception,e:
      print
      print "new error",e,page_url,value
      return None
