function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.rank = values[0];
    obj.name = values[1];
    obj.country = values[2];
    obj.points = values[3];
    obj.avg = values[4];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }