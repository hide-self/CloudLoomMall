from flask import Flask,render_template

# 1、import_name，  __name__ 也可以是 'main'
# 2、templates_folder，  这个参数修改html文件的文件夹位置，默认是templates
app = Flask('main',template_folder='templates',static_folder='public')


# 相当于创建了一个网址 /show/info 与一个函数 index() 的对应关系
# 以后用户在浏览器上访问 /show/info ，网站就自动执行 index（）函数
@app.route('/show/NyingchiStreet')
def index():
    # flask框架可以支持 return   html代码或者 html文件
    # 若想返回html文件，此时需要导入 render_template函数
    # 我们应该在当前目录下创建 templates 文件夹，在里面访问html文件

    return render_template('./templates/NyingchiStreet.html')


if __name__ == '__main__':

    # app.run(host='xxxx',port='xxxx',debug)
    # 方法中的参数 host 和 port 主机名和端口都可以自己定义
    # debug=True 表示网站是否可以边修改代码边运行
    app.run(host='127.0.0.1',port=8888,debug=True)
    # 此时访问 http://127.0.0.1:8888/show/NyingchiStreet  即可显示林芝街
    # 现在的网站代码，必须手动关闭，否则将一直运行


    