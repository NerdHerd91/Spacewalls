/*
 * Copyright (c) 2014, Facebook, Inc.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree. An additional grant
 * of patent rights can be found in the PATENTS file in the same directory.
 *
 * TodoStore
 */
var request = require('superagent');
var AppDispatcher = require('../dispatcher/AppDispatcher');
var EventEmitter = require('events').EventEmitter;
var WallConstants = require('../constants/WallConstants');
var assign = require('object-assign');

var CHANGE_EVENT = 'change';

var _photos = {};



function approve(id) {
  request.get('/api/images/approve/%d' % (id), function(data) {
    delete _photos[id];
  });
}

function decline(id) {
  request.get('/api/images/decline/%d' % (id), function(data) {
    delete _photos[id];
  });
}

var WallStore = assign({}, EventEmitter.prototype, {
  
  /**
   * Get the entire collection of TODOs.
   * @return {object}
   */
  getAll: function() {
    return _photos;
  },

  emitChange: function() {
    this.emit(CHANGE_EVENT);
    console.log('emitting');
  },

  /**
   * @param {function} callback
   */
  addChangeListener: function(callback) {
    this.on(CHANGE_EVENT, callback);
  },

  /**
   * @param {function} callback
   */
  removeChangeListener: function(callback) {
    this.removeListener(CHANGE_EVENT, callback);
  }

});

// Register callback to handle all updates
AppDispatcher.register(function(action) {
  var text;

  switch(action.actionType) {
    case WallConstants.APPROVE_IMAGE:
      approve(action.id);
      WallStore.emitChange();
      break;
    case WallConstants.DECLINE_IMAGE:
      decline(action.id);
      WallStore.emitChange();
      break;
    default:
      // no op
  }
});


request.get('/api/images', function(data) {
  _photos = JSON.parse(data.text);
  console.log(_photos);
  WallStore.emitChange();
})

module.exports = WallStore;
