/*
 * Copyright (c) 2014, Facebook, Inc.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree. An additional grant
 * of patent rights can be found in the PATENTS file in the same directory.
 *
 * TodoActions
 */

var AppDispatcher = require('../dispatcher/AppDispatcher');
var WallConstants = require('../constants/WallConstants');

var WallActions = {

  approveImage: function(id) {
    AppDispatcher.dispatch({
      actionType: WallConstants.APPROVE_IMAGE,
      id: id
    });
  },

  declineImage: function(id) {
    AppDispatcher.dispatch({
      actionType: WallConstants.DECLINE_IMAGE,
      id: id
    });
  }

};

module.exports = WallActions;
