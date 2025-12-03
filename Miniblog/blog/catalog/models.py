from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author',on_delete=models.RESTRICT, null=True)

    content = models.TextField(max_length=2000, help_text="Talk about your Blog here.")

    pub_date = models.DateTimeField()
    #comment = models.ForeignKey('Comment', null=True, on_delete=models.SET_NULL)



    def __str__(self):
            """String for representing the Model object."""
            return self.title

    def get_absolute_url(self):
            """Returns the URL to access a detail record for this book."""
            return reverse('blog_detail', args=[str(self.id)])
    

#CLASS REPRESENTING AN AUTHOR/BLOGGER
class Author(models.Model):
    user_name= models.CharField(max_length= 100)
    bio= models.TextField(max_length=1000)

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.user_name


#CLASS REPRESENTING A COMMENT FROM A USER
#IT'S A  FORM!!!
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)     
    pub_date=models.DateTimeField()
    description=models.TextField(max_length=75,
    help_text="Enter comment about the blog here")
    
    def __str__(self):
        return f"Comment on {self.blog.title}"

    