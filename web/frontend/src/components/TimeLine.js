import React from 'react';

class TimeLine extends React.Component {
    render() {
        return (
            <div>{this.props.number}</div>
        )
    }
}

TimeLine.propTypes = {
    ip_addr: React.PropTypes.string.isRequired,
    mac_addr: React.PropTypes.string.isRequired,
    intervals: React.PropTypes.array,
}

export default TimeLine