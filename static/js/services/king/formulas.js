app.factory('formulas', ['$http', function($http){
    var formulas = [
    // 0
    function(level) {
        return level + 2;
    },
    // 1
    function(level) {
        return 17 * level - Math.floor(level/3) - 1;
    },
    // 2
    function(level) {
        return (19.7 + (level - 1) * 0.3 - Math.floor(level/7)/100).toFixed(2);
    },
    // 3
    function(level) {
        return 18 * level + Math.floor((level - 1) / 3);
    },
    // 4
    function(level) {
        var x = 0;
        var temp = level;
        while(temp) {
            if (temp <= 10) {
                if (temp % 3 == 0) {
                    x += 0.01
                }
            } else {
                var y = temp % 10;
                if (y == 0 || y == 3 || y == 6) {
                    x += 0.01;
                }
            }
            temp--;
        }
        var z = 25.93 + 0.39 * (level - 1) + x
        return z.toFixed(2);
    },
    // 5
    function(level) {
        return 13 * level + Math.floor(level / 11);
    },
    // 6
    function(level) {
        var x = 15.99;
        var a = 1;
        var tag = 5;
        var y = 0;

        var increase = 0.01;
        var xx = 4;
        while(a <= level) {
            if (a == 4) {
                y += increase;
                xx += 4;
            } else

            if (a == 8) {
                y += increase;
                xx += 5;
            }
            if (a == 13) {
                    xx += 4
                    y += increase;
            }
            if (a > 13) {

                if (a == xx) {
                    y += increase;
                    if (tag > 0) {
                        if (tag == 1) {
                            xx += 1;
                        }
                        xx += 4;
                    }
                    if (tag <= 0) {
                        if (tag == -2) {
                            xx +=1;
                            tag = 5; // 后面再被 减1 回到初始的4
                        }
                        xx += 4;
                    }
                    tag--;
                }
            }

            a++;
        }
        var res = x + (level - 1) * 0.24 + y;
        return res.toFixed(2);
    },
    // 7
    function(level) {
        var base = 16.44
        var increase = 0.01;
        var step = 0.2
        var temp = 1;
        var tag = 1;
        var xx = 8;
        while(temp <= level) {

            if (temp == 4) {
                base += increase;
            } else if (temp > 4) {
                if (temp = xx) {
                    base += increase;
                    if (tag > 0) {
                        xx += 3;
                    } else {
                        xx += 4;
                        tag = 2;
                    }
                    tag--;
                }
            }

             temp++;
        }
        var res = base + (level - 1) * step;
        return res.toFixed(2);
    },
    // 8
    function(level) {
        var step = 3;
        var res = step * level + Math.floor((level -1 ) / 18)
        return res;
    },
    // 9
    function(level) {
        var base = 25.59;
        var step = 0.39;
        var increase = 0.01;
        var temp = 1;
        var tag = 2;
        var xx = 2;
        while(temp <= level) {
            if (temp == xx) {
                base -= increase;
                if (tag > 0) {
                   if (tag == 1) {
                    xx += 1;
                   }
                   xx += 4;
                } else {
                    if (tag == -2) {
                        xx += 1;
                        tag = 2;
                    }
                    xx += 4;
                }
                tag--;
            }
            temp++;
        }
        var res = base + (level - 1) * step;
        return res.toFixed(2);
    },
    // 10
    function(level) {
        return 19 + (level - 1) * 20;
    },
    // 11
    function(level) {
        return (21.83 + (level - 1) * 0.33).toFixed(2);
    },
    // 12
    function(level) {
        var base = 19.19;
        var step = 0.29
        var increase = 0.01;
        var tag = 1;
        var xx = 10;
        var temp = 1;
        while(temp <= level) {
            if (temp == xx) {
                base += increase;
                if (tag) {
                    xx += 13;
                    tag = 0;
                } else {
                    xx += 12;
                    tag = 1;
                }
            }
            temp++;
        }
        var res = base + (level - 1) * step;
        return res.toFixed(2);
    },
    // 13
    function(level) {
        var base = 38.94;
        var step = 0.39;
        var increase = 0.01;
        var res = base + (level - 1) * step;
        if (level <= 3) {
            res += increase
        } else {
            res += Math.floor((level + 1) / 3) * 0.01;
        }

        return res.toFixed(2);
    },
    // 14
    function(level) {
        var base = 10 * level;
        if (level > 1  ) {
            if (level % 2 == 1) {
                base += Math.floor(level / 2);
            } else {
                base += Math.floor(level / 2) - 1;
            }

        }
        return base;

    },
    // 15
    function(level) {
        var base = 8;
        var step = 9;
        return base + step * (level - 1) - Math.floor(level / 38);
    },
    // 16
    function(level) {
        return 30 * level + Math.floor(level / 20);
    },
    // 17
    function(level) {
        var base = 33.37;
        var step = 0.5;
        var increase = 0.01;

        if (level >= 2) {
            base += increase;
           if (level % 2 == 1) {
                base += Math.floor(level / 2) * increase;
            } else {
                base += (Math.floor(level / 2) - 1) * increase;
            }
        }
        var res = base + (level - 1) * step;
        return res.toFixed(2);
    },
    // 18
    function(level) {
        var base = 12.38;
        var step = 0.19;
        var increase = 0.01;
        var temp = 1;
        var tag = 2;
        var xx = 2;
        while(temp <= level) {
            if (temp == xx) {
                base -= increase;
                if (tag > 0) {
                   if (tag == 1) {
                    xx += 1;
                   }
                   xx += 4;
                } else {
                    if (tag == -2) {
                        xx += 1;
                        tag = 2;
                    }
                    xx += 4;
                }
                tag--;
            }
            temp++;
        }
        var res = base + (level - 1) * step;
        return res.toFixed(2);
    },
    // 19
    function(level) {
        var base = 31.18;
        var temp = level;
        var step = 0.47
        var increase = 0.01
        if (level >= 2 && level < 6) {
            base += increase
        } else if (level >= 6) {
            base += Math.floor((level - 2) / 4) * increase;
        }

        return (base + (level - 1) * step).toFixed(2);
    }
    ];


    return formulas;
}]);