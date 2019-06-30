from kotano import proxy
from static import env
from static import cdnlink


@proxy("html")
def error404(request):
    template = env.get_template("404.html")
    return template.render(cdnlink=cdnlink)
