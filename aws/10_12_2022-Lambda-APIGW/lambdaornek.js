'use strict';

exports.handler = (event, context, callback) => {
    let min = 0;
    let max = 100;

    let olusturulanRakam = Math.floor(Math.random() * max) + min;

    callback(null, olusturulanRakam);
};
