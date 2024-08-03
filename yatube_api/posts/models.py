from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Сообщество',
        help_text=(
            'Может состоять из символов латиницы и кириллицы, '
            'а также содержать цифры'
        ),
    )
    slug = models.SlugField(
        unique=True,
        max_length=50,
        verbose_name='Идентификатор',
        help_text=(
            'Может состоять только из символов латиницы в нижнем '
            'регистре, а также цифр'
        ),
    )
    description = models.TextField(
        verbose_name='Описание сообщества',
        help_text=(
            'Краткое описание.'
        ),
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст публикации',
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
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Изображение',
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

    def __str__(self):
        return self.text[:10]


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
        verbose_name='Текст комментария',
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

    def __str__(self):
        return self.text[:15]


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

    class Meta():
        constraints = (
            UniqueConstraint(
                fields=('user', 'following'),
                name='unique_follow',
            ),
        )

    def __str__(self):
        return f'{self.user.username} подписка {self.following.username}'
