/**
 * Copyright (c) 2014, Facebook, Inc.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree. An additional grant
 * of patent rights can be found in the PATENTS file in the same directory.
 */

var React = require('react');
var ReactPropTypes = React.PropTypes;
var WallActions = require('../actions/WallActions');

var cx = require('react/lib/cx');

var WallItem = React.createClass({

  getInitialState: function() {
    return {};
  },

  /**
   * @return {object}
   */
  render: function() {
    var url = this.props.photo;
    var id = this.props.id;

    // List items should get the class 'editing' when editing
    // and 'completed' when marked as completed.
    // Note that 'completed' is a classification while 'complete' is a state.
    // This differentiation between classification and state becomes important
    // in the naming of view actions toggleComplete() vs. destroyCompleted().
    return (
      <li key={id}>
        <div className="view">
          <input
            className="approve"
            type="checkbox"
            checked={false}
            onChange={this._onApproved}
          />
          <img src={url}></img>
          <button className="destroy" onClick={this._onDeclined} />
        </div>
      </li>
    );
  },

  _onApproved: function() {
    console.log(this.props);
    console.log(this.props.id);
    WallActions.approveImage(this.props.id);
  },

  _onDeclined: function() {
    WallActions.declineImage(this.props.id);
  }

});

module.exports = WallItem;
