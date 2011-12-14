#encoding:utf-8

import math

class MeshCodeUtility(object):

	#1次メッシュコードの取得
	@staticmethod
	def get_1st_mesh(lat, lon):

		left_operator  = int( math.floor(lat * 15 / 10 ) )
		right_operator = int( math.floor(lon - 100 ) )
		#南西端のlat,lon
		dest_lat = left_operator / 15 * 10.0
		dest_lon = right_operator + 100.0

		src = {"mesh_code":str(left_operator)+str(right_operator), "lat":dest_lat, "lon":dest_lon}
		return src

	#2次メッシュコードの取得
	@staticmethod
	def get_2nd_mesh(lat, lon):
		base_data = MeshCodeUtility.get_1st_mesh(lat, lon)

		#2次メッシュは緯度方向5分(5/60=0.08333)区切り
		left_operator = int(math.floor((lat - base_data["lat"]) * 100000 / 8333))
        #経度方向7分30秒(7/60+30/60/60=0.11666+0.008333=0.1249))区切り
		right_operator = int(math.floor((lon - base_data["lon"]) * 1000 / 125))
		#南西端のlat,lon
		dest_lat = left_operator * 8333 / 100000.0 + base_data["lat"]
		dest_lon = right_operator * 125 / 1000.0   + base_data["lon"]
		src = {"mesh_code":base_data["mesh_code"]+str(left_operator)+str(right_operator), "lat":dest_lat, "lon":dest_lon}
		return src

	#3次メッシュコードの取得
	@staticmethod
	def get_3rd_mesh(lat, lon):
		base_data = MeshCodeUtility.get_2nd_mesh(lat, lon)

		#3次メッシュは緯度方向 30秒(30/60/60=0.008333)区切り
		left_operator = int(math.floor((lat - base_data["lat"]) * 1000000 / 8333))
		#経度方向 45秒(45/60/60=0.0125)区切り
		right_operator = int(math.floor((lon - base_data["lon"]) * 10000 / 125))
		#南西端のlat,lon
		dest_lat = left_operator * 8333 / 1000000.0 + base_data["lat"]
		dest_lon = right_operator * 125 / 10000.0 + base_data["lon"]

		src = {"mesh_code":base_data["mesh_code"]+str(left_operator)+str(right_operator), "lat":dest_lat, "lon":dest_lon}
		return src
