from django.db import models

NULLABLE = {
    'null': True,
    'blank': True
}


class Course(models.Model):
    name = models.CharField(max_length=30, verbose_name='название')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Payments(models.Model):
    method = (('cash', 'cash'), ('card', 'card'))
    course = models.ForeignKey('course.Course', on_delete=models.SET_NULL, verbose_name='оплаченный курс',
                               related_name='payments', **NULLABLE)
    lesson = models.ForeignKey('lesson.Lesson', on_delete=models.SET_NULL, verbose_name='оплаченный урок',
                               related_name='lesson',
                               **NULLABLE)

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, max_length=50, verbose_name='пользователь',
                             related_name='users_pay')
    payment_date = models.DateTimeField(auto_created=True, verbose_name="дата оплаты", **NULLABLE)
    paid = models.BooleanField(verbose_name='оплаченный курс или урок', **NULLABLE)
    payment_amount = models.BigIntegerField(verbose_name="сумма оплаты", **NULLABLE)
    payment_method = models.CharField(max_length=10, choices=method, **NULLABLE)

    def __str__(self):
        return f'{self.user} - {self.paid}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


class Subscription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='подписка на курс')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='подписка пользователя')
    subscription = models.BooleanField(default=False, verbose_name='наличие bool')

    def __str__(self):
        return f'{self.course} , {self.user} подписка {self.subscription}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
