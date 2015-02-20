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
var WallItem = require('./WallItem.react');

var MainSection = React.createClass({

  propTypes: {
    allPhotos: ReactPropTypes.object.isRequired
  },

  /**
   * @return {object}
   */
  render: function() {
    // This section should be hidden by default
    // and shown when there are todos.
    if (Object.keys(this.props.allPhotos).length < 1) {
      return null;
    }

    var allPhotos = this.props.allPhotos;
    var photos = [];

    for (var key in allPhotos) {
      photos.push(<WallItem id={key} photo={allPhotos[key]} />);
    }

    return (
      <section id="main">
        <ul id="wallpaper-list">{photos}</ul>
      </section>
    );
  }

});

module.exports = MainSection;
