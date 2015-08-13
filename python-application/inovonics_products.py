def inovonics_product(pti): 
	ino_list = {0:{"device_type":"EN1210", "device_description":"Single Input Universal Transmitter", "mid":178, "pti":0, "inputs":1, "input_list":{"1":"Input 1"}, "supervision":900},2:{"device_type":"EN1210-60", "device_description":"Single Input Universal Transmitter (with 60 minute check-in)", "mid":178, "pti":2, "inputs":1, "input_list":{"1":"Input 1"}, "supervision":18000},6:{"device_type":"EN1210-240", "device_description":"Single Input Universal Transmitter (with 240 minute check-in)", "mid":178, "pti":6, "inputs":1, "input_list":{"1":"Input 1"}, "supervision":72000},5:{"device_type":"EN1210EOL", "device_description":"Single Input Universal Transmitter with EOL Protection", "mid":178, "pti":5, "inputs":1, "input_list":{"1":"Input 1"}, "supervision":900},4:{"device_type":"EN1210SK", "device_description":"Universal Survey Transmitter", "mid":178, "pti":4, "inputs":1, "input_list":{"1":"Input 1",}, "supervision":900},3:{"device_type":"EN1210W", "device_description":"Door/Window Transmitter with Reed Switch", "mid":178, "pti":3, "inputs":2, "input_list":{"1":"Contacts","2":"Reed Switch"}, "supervision":900},32:{"device_type":"EN1210W-60", "device_description":"Door/Window Transmitter with Reed Switch", "mid":178, "pti":32, "inputs":2, "input_list":{"1":"Contacts","2":"Reed Switch"}, "supervision":18000},1:{"device_type":"EN1212", "device_description":"Dual Input Universal Transmitter", "mid":178, "pti":1, "inputs":2, "input_list":{"1":"Contacts","2":"Reed Switch"}, "supervision":900},10:{"device_type":"EN1212-60", "device_description":"Dual Input Universal Transmitter (with 60 minute check-in)", "mid":178, "pti":10, "inputs":2, "input_list":{"1":"Input 1","2":"Input 2"}, "supervision":18000},8:{"device_type":"EN1215", "device_description":"Universal Transmitter", "mid":178, "pti":8, "inputs":1, "input_list":{"1":"Input 1"}, "supervision":900},13:{"device_type":"EN1215EOL", "device_description":"Universal Transmitter with Wall Tamper", "mid":178, "pti":13, "inputs":1, "input_list":{"1":"Input 1"}, "supervision":900},11:{"device_type":"EN1215W", "device_description":"Door/Window Transmitter with Wall Tamper", "mid":178, "pti":11, "inputs":2, "input_list":{"1":"Contacts","2":"Reed Switch"}, "supervision":900},14:{"device_type":"EN1215WEOL", "device_description":"Door/Window Transmitter with Wall Tamper, Reed Switch and EOL Protection", "mid":178, "pti":14, "inputs":2, "input_list":{"1":"Contacts","2":"Reed Switch"}, "supervision":900},9:{"device_type":"EN1216", "device_description":"Dual Input Universal Transmitter with Wall Tamper", "mid":178, "pti":9, "inputs":2, "input_list":{"1":"Contacts","2":"Reed Switch"}, "supervision":900},29:{"device_type":"EN1221S-60", "device_description":"Waterproof Pendant Transmitter (with 60 minute check-in)", "mid":178, "pti":29, "inputs":1, "input_list":{"1":"Pendant"}, "supervision":18000},25:{"device_type":"EN1223D", "device_description":"Double-Button Water-Resistant Pendant Transmitter", "mid":178, "pti":25, "inputs":1, "input_list":{"1":"Pendant"}, "supervision":900},24:{"device_type":"EN1223S", "device_description":"Single-Button Water-Resistant Pendant Transmitter", "mid":178, "pti":24, "inputs":1, "input_list":{"1":"Pendant"}, "supervision":900},26:{"device_type":"EN1223S-60", "device_description":"Single-Button Water-Resistant Pendant Transmitter", "mid":178, "pti":26, "inputs":1, "input_list":{"1":"Pendant"}, "supervision":18000},30:{"device_type":"EN1223SK", "device_description":"Pendant Survey Transmitter", "mid":178, "pti":30, "inputs":1, "input_list":{"1":"Pendant"}, "supervision":900},22:{"device_type":"EN1224", "device_description":"EN1224 Multiple Condition Pendant Transmitter", "mid":178, "pti":22, "inputs":4, "input_list":{"1":"Button 1","2":"Button 2","3":"Button 3","4":"Button 4"}, "supervision":900},23:{"device_type":"EN1224-ON", "device_description":"EN1224-ON Multiple Condition On/ Off Pendant Transmitter", "mid":178, "pti":23, "inputs":4, "input_list":{"1":"Button 1","2":"Button 2","3":"Button 3","4":"Button 4"}, "supervision":900},21:{"device_type":"EN1233D", "device_description":"Double-Button Necklace Pendant Transmitter", "mid":178, "pti":21, "inputs":1, "input_list":{"1":"Pendant"}, "supervision":900},20:{"device_type":"EN1233S", "device_description":"Single-Button Necklace Pendant Transmitter", "mid":178, "pti":20, "inputs":1, "input_list":{"1":"Pendant"}, "supervision":900},17:{"device_type":"EN1235D", "device_description":"Double-Button Belt Clip Pendant Transmitter", "mid":178, "pti":17, "inputs":1, "input_list":{"1":"Pendant"}, "supervision":900},19:{"device_type":"EN1235DF", "device_description":"Double-Button Fixed Position Hold Up Transmitter", "mid":178, "pti":19, "inputs":1, "input_list":{"1":"Pendant"}, "supervision":900},16:{"device_type":"EN1235S", "device_description":"Single-Button Belt Clip Pendant Transmitter", "mid":178, "pti":16, "inputs":1, "input_list":{"1":"Pendant"}, "supervision":900},18:{"device_type":"EN1235SF", "device_description":"Single-Button Fixed Position Hold Up Transmitter", "mid":178, "pti":18, "inputs":1, "input_list":{"1":"Pendant"}, "supervision":900},57:{"device_type":"EN1236D", "device_description":"Double-Button Three Condition Pendant Transmitter", "mid":178, "pti":57, "inputs":3, "input_list":{"1":"Button 1","2":"Button 2","3":"Both Buttons"}, "supervision":900},58:{"device_type":"EN1238D", "device_description":"Double-Button Dual Condition Pendant Transmitter", "mid":178, "pti":58, "inputs":2, "input_list":{"1":"Button 1","2":"Button 2"}, "supervision":900},49:{"device_type":"EN1240", "device_description":"Activity Sensor", "mid":178, "pti":49, "inputs":1, "input_list":{"1":"Activity"}, "supervision":900},45:{"device_type":"EN1241-60", "device_description":"Activity Sensor (with 60 minute check-in)", "mid":178, "pti":45, "inputs":1, "input_list":{"1":"Activity"}, "supervision":18000},44:{"device_type":"EN1242", "device_description":"Smoke Detector Transmitter", "mid":178, "pti":44, "inputs":1, "input_list":{"1":"Smoke Detector"}, "supervision":900},50:{"device_type":"EN1247", "device_description":"Glassbreak Detector Transmitter", "mid":178, "pti":50, "inputs":1, "input_list":{"1":"Glass Break"}, "supervision":900},48:{"device_type":"EN1249", "device_description":"Billtrap Transmitter", "mid":178, "pti":48, "inputs":1, "input_list":{"1":"Bill Trap"}, "supervision":900},7:{"device_type":"EN1252", "device_description":"Extended Range Universal Transmitter", "mid":178, "pti":7, "inputs":2, "input_list":{"1":"Input 1","2":"Input 2"}, "supervision":900},40:{"device_type":"EN1260", "device_description":"Wall Mount Motion Detector", "mid":178, "pti":40, "inputs":1, "input_list":{"1":"Motion Detector"}, "supervision":900},43:{"device_type":"EN1261HT", "device_description":"High Traffic Four Element Motion Detector", "mid":178, "pti":43, "inputs":1, "input_list":{"1":"Motion Detector"}, "supervision":900},41:{"device_type":"EN1262", "device_description":"Motion Detector with Pet Immunity", "mid":178, "pti":41, "inputs":1, "input_list":{"1":"Smoke Detector"}, "supervision":900},42:{"device_type":"EN1265", "device_description":"360 Ceiling Mount Motion Detector", "mid":178, "pti":42, "inputs":1, "input_list":{"1":"Motion Detector"}, "supervision":900},12:{"device_type":"EN1941", "device_description":"Pull Cord with Check-in and Staff Assist", "mid":178, "pti":12, "inputs":2, "input_list":{"1":"Pull Cord","2":"Staff Assist"}, "supervision":900},15:{"device_type":"EN1941-60", "device_description":"Pull Cord with Check-in and Staff Assist (with 60 minute check-in)", "mid":178, "pti":15, "inputs":2, "input_list":{"1":"Pull Cord","2":"Staff Assist"}, "supervision":18000}}
	return ino_list[pti]