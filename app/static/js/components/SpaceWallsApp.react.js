var React = require('react');
var WallStore = require('../stores/WallStore');
var WallActions = require('../actions/WallActions');
var WallItem = require('./Wallitem.react');
var MainSection = require('./MainSection.react');

function getPendingPhotos() {
    return {
        allPhotos: WallStore.getAll()
    };
}

var SpaceWallsApp = React.createClass({
    getInitialState: function() {
        return getPendingPhotos();
    },

    componentDidMount: function() {
        WallStore.addChangeListener(this._onChange);
    },

    componentWillUnmount: function() {
        WallStore.removeChangeListener(this._onChange);
    },

    render: function() {
        return (
            <div>
                <MainSection allPhotos={this.state.allPhotos}/>
            </div>
        );
    },

    _onChange: function() {
        this.setState(getPendingPhotos());
    }
});

module.exports = SpaceWallsApp;