srt = 'https://images.unsplash.com/photo-1491974162517-a7541284efe7?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=e0c4664b504f632d31f49fb757f9335f&w=1000&q=80'
width_pos = srt.index('&w=')
height_pos = srt.index('&q=')
width_height_str = srt[width_pos :] #使用切片功能截取高度和宽度参数，后面用来将该参数替换掉
print('高度和宽度数据字符串是：', width_height_str)
img_url_final = srt.replace(width_height_str, '')  #把高度和宽度的字符串替换成空字符
print('截取后的图片的url为：', img_url_final)
