# china-high-speed-rail-map_site_python
中国高铁地图网。在中国地图上展示中国各条高铁线路。是一个用python语种，利用web.py框架开发的一个小型高铁地图网。此为原项目https://github.com/KermitCode/china-gaotie-map_python_web.py 的一个简化处理版本，去除了省份、城市、高铁站、高铁知识内容等没有用的东西。此版本高铁后台只包括高铁线路的新增修改、每条高铁线路各站点的快速增加编辑。前台拿到每条线路各站点的经纬度后在百度地图上展示。可访问URL地址： http://gaotie.04007.cn/ 前台展示效果截图如下：
<img src="https://github.com/KermitCode/china-high-speed-rail-map_site_python/blob/master/%E4%B8%AD%E5%9B%BD%E9%AB%98%E9%93%81%E5%9C%B0%E5%9B%BE-%E4%B8%AD%E5%9B%BD%E9%AB%98%E9%93%81%E7%BA%BF%E8%B7%AF%E5%9B%BE.jpg?raw=true">
后台编辑页面地址：http://gaotie.04007.cn/line  截图如下：
<img src="https://github.com/KermitCode/china-high-speed-rail-map_site_python/blob/master/%E9%AB%98%E9%93%81%E5%A4%A7%E5%85%A8%E7%AE%A1%E7%90%86%E5%90%8E%E5%8F%B0.jpg?raw=true">
具体每条线路的编辑时，输入高铁站点名字，后台直接去百度地图查询此关键词的经纬度数据并完成填充，有时会出现重名错误，需要人工介入编辑，可以参考每个站点的上下站点经纬度数据，因为相差极小，页面截图如下：
<img src="https://github.com/KermitCode/china-high-speed-rail-map_site_python/blob/master/%E9%AB%98%E9%93%81%E5%A4%A7%E5%85%A8%E7%AE%A1%E7%90%86%E5%90%8E%E5%8F%B0-%E7%BA%BF%E8%B7%AF%E7%BC%96%E8%BE%91.jpg?raw=true">
简化后只需要两张数据表即可。见sql附件
