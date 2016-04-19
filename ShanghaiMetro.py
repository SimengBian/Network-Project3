#line1 = {"Fujin Road":0,"West Youyi Road":1,"Bao'an Highway":2,"Gongfu Xincun":3,"Hulan Road":4,"Tonghe Xincun":5,"Gongkang Road":6,"Pengpu Xincun":7,"Wenshui Road":8,"Shanghai Circus World":9,"Yanchang Road":10,"North Zhongshan Road":11,"Shanghai Railway Station":12,"Hanzhong Road":13,"Xinzha Road":14,"People's Square":15,"South Huangpi Road":16,"South Shaanxi Road":17,"Changshu Road":18,"Hengshan Road":19,"Xujiahui":20,"Shanghai Indoor Stadium":21,"Caobao Road":22,"Shanghai South Railway Station":23,"Jinjiang Park":24,"Lianhua Road":25,"Waihuanlu":26,"Xinzhuang":27}
line1 = ["Fujin Road","West Youyi Road","Bao'an Highway","Gongfu Xincun","Hulan Road","Tonghe Xincun","Gongkang Road","Pengpu Xincun","Wenshui Road","Shanghai Circus World","Yanchang Road","North Zhongshan Road","Shanghai Railway Station","Hanzhong Road","Xinzha Road","People's Square","South Huangpi Road","South Shaanxi Road","Changshu Road","Hengshan Road","Xujiahui","Shanghai Indoor Stadium","Caobao Road","Shanghai South Railway Station","Jinjiang Park","Lianhua Road","Waihuanlu","Xinzhuang"]
line1_time = [2,2,3,3,2,3,2,3,3,2,2,2,1,2,2,3,2,2,2,2,3,2,3,3,3,2,2]
#line2 = {"East Xujing":28,"Hongqiao Railway Station":29,"Hongqiao Airport Terminal 2":30,"Songhong Road":31,"Beixinjing":32,"Weining Road":33,"Loushanguan Road":34,"Zhongshan Park":35,"Jiangsu Road":36,"Jing'an Temple":37,"West Nanjing Road":38,"People's Square":39,"East Nanjing Road":40,"Lujiazui":41,"Dongchang Road":42,"Century Avenue":43,"Shanghai Science & Technology":44,"Century Park":45,"Longyang Road":46,"Zhangjiang High Technology Park":47,"Jinke Road":48,"Guanglan Road":49,"Tangzhen":50,"Middle Chuangxin Road":51,"East Huaxia Road":52,"Chuansha":53,"Lingkong Road":54,"Yuandong Avenue":55,"Haitiansan Road":56,"Pudong International Airport":57}
line2 = ["East Xujing","Hongqiao Railway Station","Hongqiao Airport Terminal 2","Songhong Road","Beixinjing","Weining Road","Loushanguan Road","Zhongshan Park","Jiangsu Road","Jing'an Temple","West Nanjing Road","People's Square","East Nanjing Road","Lujiazui","Dongchang Road","Century Avenue","Shanghai Science & Technology","Century Park","Longyang Road","Zhangjiang High Technology Park","Jinke Road","Guanglan Road","Tangzhen","Middle Chuangxin Road","East Huaxia Road","Chuansha","Lingkong Road","Yuandong Avenue","Haitiansan Road","Pudong International Airport"]
line2_time = [3,2,7,2,2,3,3,2,3,2,3,2,3,2,2,3,2,2,4,3,2,4,4,4,3,4,4,5,7]
#line3 = {"North Jiangyang Road":58,"Tieli Road":59,"Youyi Road":60,"Baoyang Road":61,"Shuichan Road":62,"Songbin Road":63,"Zhanghuabang":64,"Songfa Road":65,"South Changjiang Road":66,"West Yingao Road":67,"Jiangwan Town":68,"Dabaishu":69,"Chifeng Road":70,"Hongkou Football Stadium":71,"Dongbaoxing Road":72,"Baoshan Road":73,"Shanghai Railway Station":74,"Zhongtan Road":75,"Zhenping Road":76,"Caoyang Road":77,"Jinshajiang Road":78,"Zhongshan Park":79,"West Yan'an Road":80,"Hongqiao Road":81,"Yishan Road":82,"Caoxi Road":83,"Longcao Road":84,"Shilong Road":85,"Shanghai South Railway Station":86}
line3 = ["North Jiangyang Road","Tieli Road","Youyi Road","Baoyang Road","Shuichan Road","Songbin Road","Zhanghuabang","Songfa Road","South Changjiang Road","West Yingao Road","Jiangwan Town","Dabaishu","Chifeng Road","Hongkou Football Stadium","Dongbaoxing Road","Baoshan Road","Shanghai Railway Station","Zhongtan Road","Zhenping Road","Caoyang Road","Jinshajiang Road","Zhongshan Park","West Yan'an Road","Hongqiao Road","Yishan Road","Caoxi Road","Longcao Road","Shilong Road","Shanghai South Railway Station"]
line3_time = [2,3,2,3,2,2,2,3,3,3,2,2,3,2,2,4,2,3,2,2,3,2,2,2,3,2,2,2]

edges = {}
nodes = set()
previous = {} 
distance = {}
MAX_VALUE = 10000
start = ""
end = ""

def construct():
	global edges
	global nodes
	for i in range(len(line1)-1):
		edges[(line1[i],line1[i+1])] = ["line1",line1_time[i]]
		nodes.add(line1[i])
	nodes.add(line1[i])
	for i in range(len(line2)-1):
		edges[(line2[i],line2[i+1])] = ["line2",line2_time[i]]
		nodes.add(line2[i])
	nodes.add(line2[i])
	for i in range(len(line3)-1):
		edges[(line3[i],line3[i+1])] = ["line3",line3_time[i]]
		nodes.add(line3[i])
	nodes.add(line3[i])

	
def dijkstra(start):
	global previous # {1:1,2:1,3:2,4:8,...}   des node : previous node
	global distance # {1:0,2:2,3:5,4:8,...}   des node : distance
	previous = {node: [] for node in nodes} # maybe multi path
	distance = {}
	for node in nodes:
		if edges.has_key((start,node)):
			distance[node] = edges[(start,node)][1]
			previous[node].append(start)
		elif edges.has_key((node,start)):
			distance[node] = edges[(node,start)][1]
			previous[node].append(start)
		else:
			distance[node] = MAX_VALUE
	S = set([start]) # has been visited
	U = nodes-S# has not been visited

	def get_min():
		min_value = MAX_VALUE
		for node in U:
			if distance[node] < min_value:
				min_value = distance[node]
				min_node = node
				min_dist = min_value
		return min_node,min_dist
	def update():
		S.add(min_node)
		U.remove(min_node)
		for node in U:
			value = MAX_VALUE
			if edges.has_key((min_node,node)):
				value = edges[(min_node,node)][1]
			elif edges.has_key((node,min_node)):
				value = edges[(node,min_node)][1]
			if value<MAX_VALUE and distance[node] >= distance[min_node] + value:
				distance[node] = distance[min_node] + value
				previous[node].append(min_node)
	
	while(len(U)):
		(min_node,min_dist) = get_min()
		update()

def get_path():
	dest = end
	src =start
	path = []
	path.append(dest)
	while(dest!=src):
		path.append(previous[dest][0])
		dest=previous[dest][0]
	return path[::-1]

def perf_print(path):
	print "Get on at ",path[0]
	pre_line = (edges[(path[0],path[1])][0] if edges.has_key((path[0],path[1])) else edges[(path[1],path[0])][0])
	pre_station = path[0]
	now_line = pre_line
	now_station = pre_station
	print "Take ",now_line
	for i in range(len(path)-1):
		now_line = (edges[(path[i],path[i+1])][0] if edges.has_key((path[i],path[i+1])) else edges[(path[i+1],path[i])][0])
		now_station = path[i]
		if now_line!=pre_line:
			print "Get off at ",now_station
			print "Take ",now_line
			pre_station = now_station # the last station when switching
		pre_line = now_line
	print "Get off at ",end

if __name__ == '__main__':
	construct()
	# start = "Jinjiang Park"
	# end = "Lujiazui"
	while True:
		while True:
			start = raw_input("\nPlease input the start station:")
			if(start in nodes):
				break
			else:
				print "The start station is invalid!"

		while True:
			end = raw_input("\nPlease input the destination station:")
			if(end in nodes):
				break
			else:
				print "The end station is invalid!"
				
		dijkstra(start)
		path = get_path()
		perf_print(path)
	# print "The shortest path from ",start,"to ",end,"is : "
	# for s in path:
	# 	print s
	# print "The shorest time is : ",distance[end]