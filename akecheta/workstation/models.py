from django.db import models

# Create your models here.


class Server(models.Model):
    '''
    namespace

    deployment
    cronjob
    job
    daemonset

    'servive-group'
    ingress
    '''
    pass


class Ingress(models.Model):
    pass


class Pod(models.Model):
    IMAGE_PULL_POLICY = (
        (1, 'Always'),
        (2, 'IfNotPresent'),
    )

    POD_TYPE = (
        (1, '初始化容器组'),
        (2, '普通容器组'),
    )
    pod_type = models.PositiveIntegerField(default=1, choices=POD_TYPE, verbose_name='容器组类型')
    name = models.CharField(max_length=50, blank=False, verbose_name='应用名称')
    image_responstry = models.ForeignKey('Registry', verbose_name='镜像源地址', null=True, on_delete=models.SET_NULL)
    image_package = models.CharField(max_length=50, blank=False, verbose_name='镜像仓库名称')
    image_name = models.CharField(max_length=50, blank=False, verbose_name='镜像名称')
    image_versiontag = models.CharField(max_length=20, blank=False, verbose_name='镜像版本')
    image_pull_policy = models.PositiveIntegerField(default=1, choices=IMAGE_PULL_POLICY, verbose_name='镜像拉取策略')
    launch_env = models.ManyToManyField('Secret', blank=True, verbose_name='容器环境变量')
    launch_volume = models.ManyToManyField('ConfigMap', blank=True, verbose_name='容器挂载卷')
    launch_command = models.CharField(max_length=100, blank=True, verbose_name='容器启动命令')
    launch_args = models.CharField(max_length=100, blank=True, verbose_name='容器启动参数')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '容器组模型'
        ordering = ['-created_time']


class Deployment(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='applicaiton name')
    namespace = models.ForeignKey('Namespace', blank=True, null=True, verbose_name='命名空间', on_delete=models.SET_NULL)
    pod = models.ForeignKey('Pod', verbose_name='所管理容器', on_delete=models.CASCADE)
    init_pod = models.ForeignKey('Pod', verbose_name='所管理初始化容器', null=True, on_delete=models.CASCADE, related_name='init_pod_deployment')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = 'Deployment模型'
        ordering = ['-created_time']


class DaemonSet(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='applicaiton name')
    namespace = models.ForeignKey('Namespace', blank=True, null=True, verbose_name='命名空间', on_delete=models.SET_NULL)
    pod = models.ForeignKey('Pod', verbose_name='所管理容器', on_delete=models.CASCADE)
    init_pod = models.ForeignKey('Pod', verbose_name='所管理初始化容器', null=True, on_delete=models.CASCADE, related_name='init_pod_demaonset')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = 'DaemonSet模型'
        ordering = ['-created_time']



class CronJob(models.Model):
    pass


class Job(models.Model):
    pass

    def __str__(self):
        return self.name


class Namespace(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='命名空间')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = 'Namespace'
        ordering = ['-created_time']


class Registry(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='镜像源名称')
    address = models.CharField(max_length=50, blank=False, verbose_name='镜像源IP:PORT')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '镜像源仓库'
        ordering = ['-created_time']


class Secret(models.Model):
    name = models.CharField(max_length=40, blank=False, verbose_name='私密字典名')
    key_value_dict = models.CharField(max_length=100, blank=False, verbose_name='私密字典-Key:Value')
    namespace = models.ForeignKey('Namespace', blank=True, null=True, verbose_name='命名空间', on_delete=models.SET_NULL)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = 'Secret'
        ordering = ['-created_time']


class ConfigMap(models.Model):
    CONFIG_TYPE = (
        (1, 'hostpath'),
        (2, '待支持中...')
    )
    name = models.CharField(max_length=50, blank=False, verbose_name='ConfigMap名称')
    namespace = models.ForeignKey('Namespace', blank=True, null=True, verbose_name='命名空间', on_delete=models.SET_NULL)
    filepath = models.CharField(max_length=200, blank=False, verbose_name='挂载点路径')
    sub_path = models.CharField(max_length=100, blank=True, verbose_name='作为子文件的名称')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = 'ConfigMap'
        ordering = ['-created_time']
