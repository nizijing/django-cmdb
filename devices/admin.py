from django.contrib import admin
from .models import ProInfo, DeviceInfo, UnitInfo, AppInfo
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class DeviceInfoResource(resources.ModelResource):
	class Meta:
		model = DeviceInfo


class AppInfoInline(admin.TabularInline):
	model = AppInfo
	extra = 0


class UnitInfoInline(admin.TabularInline):
	model = UnitInfo
	extra = 0


class DeviceInfoInline(admin.TabularInline):
	 model = DeviceInfo
	 extra = 0


@admin.register(ProInfo)
class ProInfoAdmin(admin.ModelAdmin):
	inlines	 = (UnitInfoInline, AppInfoInline, DeviceInfoInline)
	list_display	= ('pro_name', 'pro_type', 'pro_ctime', 'pro_link', 'note')
	search_fields	= ('pro_name', )
	search_list	= ('pro_type')


@admin.register(DeviceInfo)
class DevicesAdmin(ImportExportModelAdmin):
	list_display	= ('pro', 'hostname', 'ip', 'unit_name', 'isvhost', 'hostDevice', 'os_name', 'nature', 'note')
	search_fields	= ('pro', )
	resource_class  = DeviceInfoResource




