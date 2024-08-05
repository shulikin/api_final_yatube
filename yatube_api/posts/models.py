from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import UniqueConstraint

DISPLAY_POSTS: int = 10
DISPLAY_COMMENTS: int = 15

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        'Сообщество',
        max_length=200,
        help_text=(
            'Может состоять из символов латиницы и кириллицы, '
            'а также содержать цифры. Не более 200 символов.'
        ),
    )
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        max_length=50,
        help_text=(
            'Может состоять только из символов латиницы в нижнем '
            'регистре, а также цифр. Не более 50 символов.'
        ),
    )
    description = models.TextField(
        'Описание сообщества',
        help_text=(
            'Краткое описание.'
        ),
    )

    class Meta:
        verbose_name = 'сообщество'
        verbose_name_plural = 'Сообщества'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        'Текст публикации',
        help_text=(
            'Обязательное поле.'
        ),
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        help_text=(
            'Добавление новой публикации в коллекцию публикаций.'
        ),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор записи',
        help_text=(
            'Только автор записи имеет'
            'права на её редактирование'
        ),
    )
    image = models.ImageField(
        'Изображение',
        upload_to='posts/',
        blank=True,
        help_text='Изображение для поста.',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.text[:DISPLAY_POSTS]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',
        help_text=(
            'Только автор комментария имеет'
            'права на его редактирование'
        ),
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост',
        help_text='Публикация к которой создан комментарий.',
    )
    text = models.TextField(
        'Текст комментария',
        help_text='Добавление нового комментария к публикации.',
    )
    created = models.DateTimeField(
        'Дата опубликования',
        auto_now_add=True,
        db_index=True,
        help_text=(
            'Дата создания комментария.'
            'По умолчанию - текущая дата '
        ),
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:DISPLAY_COMMENTS]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        related_name='follower',
        on_delete=models.CASCADE,
        verbose_name='Подписчик',
    )
    following = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            UniqueConstraint(
                fields=('user', 'following'),
                name='unique_follow',
            ),
        )

    def clean(self):
        if self.user == self.following:
            raise ValidationError('Действие недопустимо!')

    def __str__(self):
        return f'{self.user.username} подписка {self.following.username}'
