from django import template

register = template.Library()


def render_curency(value):
    return "ok"

@register.filter
def comment_isliked(comment,request):

    lik = comment.isLiked.filter(user=request.user).first()
    return ((lik != None) and (lik.likes) )

@register.filter
def is_ownerComent(comment,request):
    return (comment.user  == request.user )

register.filter('render_curency',render_curency)