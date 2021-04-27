from libs.webserver.executer import Executer

from flask import Blueprint, request, jsonify
from flask_login import login_required

system_info_api = Blueprint('system_info_api', __name__)


#################################################################

# /api/system/performance
# return
# {
#   "system": {
#     "cpu_info": {
#       "frequency": float,
#       "percent": float
#     },
#     "disk_info": {
#       "free": int,
#       "percent": float,
#       "total": int,
#       "used": int
#     },
#     "memory_info": {
#       "available": int,
#       "free": int,
#       "percent": float,
#       "total": int,
#       "used": int
#     },
#     "network_info": [
#       {
#         "address": str
#         "bytes_recv": int,
#         "bytes_sent": int,
#         "name": str,
#         "netmask": str
#       },
#       ...
#     ]
#   }
# }
@system_info_api.route('/api/system/performance', methods=['GET'])
@login_required
def get_system_info_performance():  # pylint: disable=E0211
    if request.method == 'GET':
        data_out = dict()

        data = Executer.instance.system_info_executer.get_system_info_performance()
        data_out["system"] = data

        if data is None:
            return "Could not find data value: data", 403
        else:
            return jsonify(data_out)


#################################################################

# /api/system/temperature
# return
# {
#   "system": {
#     "raspi": {
#       "celsius": float,
#       "fahrenheit": float
#     }
#   }
# }
@system_info_api.route('/api/system/temperature', methods=['GET'])
@login_required
def get_system_info_temperature():  # pylint: disable=E0211
    if request.method == 'GET':
        data_out = dict()

        data = Executer.instance.system_info_executer.get_system_info_temperature()
        data_out["system"] = data

        if data is None:
            return "Could not find data value: data", 403
        else:
            return jsonify(data_out)


#################################################################

# /api/system/services
# return
# {
#   "services": [
#     str,
#     ...
#   ]
# }
@system_info_api.route('/api/system/services', methods=['GET'])
@login_required
def get_services():  # pylint: disable=E0211
    if request.method == 'GET':
        data_out = dict()

        data = Executer.instance.system_info_executer.get_services()
        data_out["services"] = data

        if data is None:
            return "Could not find data value: data", 403
        else:
            return jsonify(data_out)


#################################################################

# /api/system/services/status
# return
# {
#   "services": [
#     {
#       "name": str,
#       "not_found": bool,
#       "running": bool,
#       "status": int
#     },
#    ...
#   ]
# }
@system_info_api.route('/api/system/services/status', methods=['GET'])
@login_required
def get_system_info_services():  # pylint: disable=E0211
    if request.method == 'GET':
        data_out = dict()

        data = Executer.instance.system_info_executer.get_system_info_services()
        data_out["services"] = data

        if data is None:
            return "Could not find data value: data", 403
        else:
            return jsonify(data_out)


#################################################################

# /api/system/devices/status
# return
# {
#   "devices": [
#     {
#       "connected": bool,
#       "id": str,
#       "name": str
#     },
#     ...
#   ]
# }
@system_info_api.route('/api/system/devices/status', methods=['GET'])
@login_required
def get_system_info_device_status():  # pylint: disable=E0211
    if request.method == 'GET':
        data_out = dict()
        data = Executer.instance.system_info_executer.get_system_info_device_status()
        data_out["devices"] = data

        if data is None:
            return "Could not find data value: data", 403
        else:
            return jsonify(data_out)