from django.db import models


class Book(models.Model):
    """
    Model for books.
    """
    title = models.CharField("Book Title", max_length=200)
    description = models.TextField("Description")
    cover_image = models.ImageField("Cover Image", upload_to='books/')
    
    # Technical fields
    created_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField("Visible on site", default=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['-created_at'] # Newest books first

    def __str__(self):
        return self.title
    

class PurchaseLink(models.Model):
    """
    Specific links for buying the book (Amazon, FNAC, etc.)
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='links')
    platform_name = models.CharField("Platform Name", max_length=50, help_text="e.g. Amazon, FNAC, Publisher")
    url = models.URLField("URL")

    class Meta:
        verbose_name = "Purchase Link"
        verbose_name_plural = "Purchase Links"

    def __str__(self):
        return f"{self.platform_name} link for {self.book.title}"