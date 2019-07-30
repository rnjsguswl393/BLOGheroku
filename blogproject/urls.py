
from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogapp.views.home,name="home"),
    path('blog/', include('blogapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('portfolio/',portfolio.views.portfolio,name="portfolio"),
    path('portfolio/new',portfolio.views.new,name="newportfolio"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #외부에서 자료를 받기때문에 
