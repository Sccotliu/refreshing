
/*
* Date Format 1.2.3
* (c) 2007-2009 Steven Levithan <stevenlevithan.com>
* MIT license
*
* Includes enhancements by Scott Trenda <scott.trenda.net>
* and Kris Kowal <cixar.com/~kris.kowal/>
*
* Accepts a date, a mask, or a date and a mask.
* Returns a formatted version of the given date.
* The date defaults to the current date/time.
* The mask defaults to dateFormat.masks.default.
*/
function Class() { }
Class.prototype.construct = function() {};
Class.extend = function(def) {
    var classDef = function() {
        if (arguments[0] !== Class) { this.construct.apply(this, arguments); }
    };
    
    var proto = new this(Class);
    var superClass = this.prototype;
    
    for (var n in def) {
        var item = def[n];                        
        if (item instanceof Function) item.$ = superClass;
        proto[n] = item;
    }

    classDef.prototype = proto;
    
    //赋给这个新的子类同样的静态extend方法 
    classDef.extend = this.extend;        
    return classDef;
};

var dateFormat = function() {
    var token = /d{1,4}|m{1,4}|yy(?:yy)?|([HhMsTt])\1?|[LloSZ]|"[^"]*"|'[^']*'/g,
        timezone = /\b(?:[PMCEA][SDP]T|(?:Pacific|Mountain|Central|Eastern|Atlantic) (?:Standard|Daylight|Prevailing) Time|(?:GMT|UTC)(?:[-+]\d{4})?)\b/g,
        timezoneClip = /[^-+\dA-Z]/g,
        pad = function(val, len) {
            val = String(val);
            len = len || 2;
            while (val.length < len) val = "0" + val;
            return val;
        };

    // Regexes and supporting functions are cached through closure
    return function(date, mask, utc) {
        var dF = dateFormat;

        // You can't provide utc if you skip other args (use the "UTC:" mask prefix)
        if (arguments.length == 1 && Object.prototype.toString.call(date) == "[object String]" && !/\d/.test(date)) {
            mask = date;
            date = undefined;
        }

        // Passing date through Date applies Date.parse, if necessary
        date = date ? new Date(date) : new Date;
        if (isNaN(date)) throw SyntaxError("invalid date");

        mask = String(dF.masks[mask] || mask || dF.masks["default"]);

        // Allow setting the utc argument via the mask
        if (mask.slice(0, 4) == "UTC:") {
            mask = mask.slice(4);
            utc = true;
        }

        var _ = utc ? "getUTC" : "get",
            d = date[_ + "Date"](),
            D = date[_ + "Day"](),
            m = date[_ + "Month"](),
            y = date[_ + "FullYear"](),
            H = date[_ + "Hours"](),
            M = date[_ + "Minutes"](),
            s = date[_ + "Seconds"](),
            L = date[_ + "Milliseconds"](),
            o = utc ? 0 : date.getTimezoneOffset(),
            flags = {
                d: d,
                dd: pad(d),
                ddd: dF.i18n.dayNames[D],
                dddd: dF.i18n.dayNames[D + 7],
                m: m + 1,
                mm: pad(m + 1),
                mmm: dF.i18n.monthNames[m],
                mmmm: dF.i18n.monthNames[m + 12],
                yy: String(y)
                    .slice(2),
                yyyy: y,
                h: H % 12 || 12,
                hh: pad(H % 12 || 12),
                H: H,
                HH: pad(H),
                M: M,
                MM: pad(M),
                s: s,
                ss: pad(s),
                l: pad(L, 3),
                L: pad(L > 99 ? Math.round(L / 10) : L),
                t: H < 12 ? "a" : "p",
                tt: H < 12 ? "am" : "pm",
                T: H < 12 ? "A" : "P",
                TT: H < 12 ? "AM" : "PM",
                Z: utc ? "UTC" : (String(date)
                    .match(timezone) || [""])
                    .pop()
                    .replace(timezoneClip, ""),
                o: (o > 0 ? "-" : "+") + pad(Math.floor(Math.abs(o) / 60) * 100 + Math.abs(o) % 60, 4),
                S: ["th", "st", "nd", "rd"][d % 10 > 3 ? 0 : (d % 100 - d % 10 != 10) * d % 10]
            };

        return mask.replace(token, function($0) {
            return $0 in flags ? flags[$0] : $0.slice(1, $0.length - 1);
        });
    };
}();

// Some common format strings
dateFormat.masks = {
    "default": "ddd mmm dd yyyy HH:MM:ss",
    shortDate: "m/d/yy",
    mediumDate: "mmm d, yyyy",
    longDate: "mmmm d, yyyy",
    fullDate: "dddd, mmmm d, yyyy",
    shortTime: "h:MM TT",
    mediumTime: "h:MM:ss TT",
    longTime: "h:MM:ss TT Z",
    isoDate: "yyyy-mm-dd",
    isoTime: "HH:MM:ss",
    isoDateTime: "yyyy-mm-dd'T'HH:MM:ss",
    isoUtcDateTime: "UTC:yyyy-mm-dd'T'HH:MM:ss'Z'"
};

// Internationalization strings
dateFormat.i18n = {
    dayNames: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
    monthNames: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
};

// For convenience...
Date.prototype.format = function(mask, utc) {
    return dateFormat(this, mask, utc);
};

//JavaScript Trim Functio 
String.prototype.Trim = function() 
{ 
	return this.replace(/(^\s*)|(\s*$)/g, ""); 
}

String.prototype.format = function()
{
    var args = arguments;
    return this.replace(/\{(\d+)\}/g,               
        function(m,i){
            return args[i];
        });
}

function s4() {
  return Math.floor((1 + Math.random()) * 0x10000)
             .toString(16)
             .substring(1);
};

function guid() {
  return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
         s4() + '-' + s4() + s4() + s4();
}

/*
 * @auth:l10n_rd
 * @date:4/10/2013
 * */
Array.prototype.foreach = function(callback) {
	for(var i = 0; i < this.length; i++) {
		callback(this[i], i);
	}
}

Array.prototype.popfromhead = function() {
	var result = this[0];
	this.splice(0,1);
	return result;
}

Array.prototype.getElement = function(proto_name, value) {
	for(var i = 0;i<this.length;i++) {
		if (eval("this[i].{0}".format(proto_name)) == value) return this[i];
	}
	return null;
}

Array.prototype.contains = function(element) {
	for (var i = 0; i < this.length; i++ ) {
		if (this[i] == element) {
			return true;
		}
	}
	return false;
}

Array.prototype.distinct = function(){
	var b=[];
	var obj={};
	for(var i=0;i<this.length;i++){
		obj[this[i]]=this[i];
	}
	for(var a in obj){
		b.push(obj[a]);
	}
	return b;
};

function bubbleSort(arr, attr){
  var i=arr.length, j;
  var tempExchangVal;
  while(i>0){
    for(j=0;j<i-1;j++){
    	var code1 = eval("arr[j].{0}".format(attr))[0].charCodeAt();
		var code2 = eval("arr[j+1].{0}".format(attr))[0].charCodeAt();
      if(code1>code2){
        tempExchangVal = arr[j];
        arr[j]=arr[j+1];
        arr[j+1]=tempExchangVal;
      }
    }
    i--;
  }
  return arr;
}

Array.prototype.sortbyattribute = function(attr) {
	return bubbleSort(this.slice(0), attr);
}

// 
function isarray(o) {  
  return Object.prototype.toString.call(o) === '[object Array]';   
}  

var serialtostring = function(xmldata) {
	if(xmldata.xml){//
      //alert("IE:"+xmldata.xml);
	  return xmldata.xml;
	}else{
		  //alert(("Firefox:"+new XMLSerializer().serializeToString(xmldata));
		return new XMLSerializer().serializeToString(xmldata);
	}
}

function objectisempty(obj) {
	for (var i in obj) {
		return true;
	}
	return false;
}

var fmt = {
	JSON:'json',
	XML:'xml',
	HTML:'html',
	ARRAY:'arr'
};

function SerialerManager(data) {
	this.d = data;
	this.data_format = data.data_format;
	this.ExtFUNCTION = {
		SERIALTOJSON:'serialtojson',
		SERIALTOXML:'serialtoxml',
		SERIALTOARRAY:'serialtoarr',
		SERIALTOHTML:'serialtohtml'
	};
	this.METHOD = {
		json:'serialtojson',
		xml:'serialtoxml',
		arr:'serialtoarr',
		html:'serialtohtml'
	};
	this.GETDATAFUNCTION = {
		json:function(cbfun) {return cbfun({data:eval('(' + data.content + ')'), parentId:0, id:1});},
		xml:function(cbfun) {
			var json = xmlserialtojson(parseXml(data.content).documentElement);
			return cbfun({data:json, parentId:0, id:1});
		},
		arr:function(cbfun) {return eval( data.content );}
	};
};

SerialerManager.prototype.serialtoarr = function(tree) {
	return tree.serialtoarray();
}

SerialerManager.prototype.getData = function(cbfun) {
	return this.GETDATAFUNCTION[this.d.data_format](cbfun);
}

SerialerManager.prototype.appendfunction = function(name, fun) {
	SerialerManager.prototype[name] = fun;
}

SerialerManager.prototype.serialtotargetfmt = function(tree) {
	if (SerialerManager.prototype[this.METHOD[this.d.data_format]] == undefined)
		alert("method {0} is not defined!".format(this.METHOD[this.d.data_format]));
	return SerialerManager.prototype[this.METHOD[this.d.data_format]](tree);
}

SerialerManager.prototype.setdataformat = function(fmt) {
	this.data_format = fmt;
	this.d.data_format = fmt;
}
SerialerManager.prototype.save = function(savefun) {
	savefun(this.d);
}

function TagAttribute(id, attr) {
	this.newId = id;
	this.name = attr["name"];
	this.content = attr["content"];
	this.marked = attr["mark"]
}

function UserData(data) {
	//alert(JSON.stringify(data))
	this.sourceData = data;
	this.attributes = [];
	this.text = "";
	this.comment = "";
	this.tail = "";
	if (typeof(data) == 'undefined')
		throw "the data is undefined,please set empty data to tree";
	for (var i = 0; i < data.length; i++) {
		if (data[i]["name"] != "#text" && data[i]["name"] != "comment" &&
			data[i]["name"] != "#tail") {
			var attr = new TagAttribute(i, data[i]);
			this.attributes.push(attr)
		} else if (data[i]["name"] == "#text") {
			this.text = data[i]["content"];
		} else if (data[i]["name"] == "#tail") {
			this.tail = data[i]["content"];
		} else if (data[i]["name"] == "comment") {
			this.comment = data[i]["content"];
		}
	}
}

UserData.prototype.getcommentOrText = function() {
	if (this.text != "") return this.text;
	else if (this.comment != "") return this.comment;
	else return "";
}

UserData.prototype.reset = function() {
	this.comment = "";
	this.text = "";
	this.tail = "";
}

function getElementByAttrForElements(elements, mark, text) {
	for(var i = 0; i < elements.length; i++) {
		el = elements[i];
		if ($(el).attr(mark) == text)
			return el;
	}
	return null;
}

/*
 * @ description: URL method collection
 * */
function geturlparams(url, paras){
	var paraString = url.substring(url.indexOf("?")+1,url.length).split("&"); 
    var paraObj = {} 
    for (i=0; j=paraString[i]; i++){ 
    	paraObj[j.substring(0,j.indexOf("=")).toLowerCase()] = j.substring(j.indexOf("=")+1,j.length); 
    } 
    var returnValue = paraObj[paras.toLowerCase()]; 
    if(typeof(returnValue)=="undefined"){ 
   		return ""; 
    }else{ 
    	return returnValue; 
    } 
}

function request(paras)
{ 
    var url = location.href; 
    return geturlparams(url, paras);
}

function seturlparam(url, paras) {
	var qs = "";
	for (var p in paras) {
		qs += "&{0}={1}".format(p, paras[p])
	}
	var urlParam = /.*?\?.*?/g;
	if (urlParam.exec(url)) {
		return "{0}&{1}".format(url, qs.substring(1))
		
	}else{
		return "{0}?{1}".format(url, qs.substring(1))
	}
}

if (typeof($) != "undefined") {
	$.url = {
		param:function(__name__) {
			return request(__name__);
		},
		setup:function(url, cfg) {
			return seturlparam(url, cfg);
		}
	}
}






























