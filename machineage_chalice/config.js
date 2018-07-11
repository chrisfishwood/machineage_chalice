"use strict";

var config = {
    "templateBucket" : "machineage-email-template",
    "templateKey" : "Template.html",
    "targetAddress" : "csteinmeyer@gmail.com",
    "fromAddress": "csteinmeyer@gmail.com",
    "defaultSubject" : "Email From {{name}}"
}

module.exports = config
