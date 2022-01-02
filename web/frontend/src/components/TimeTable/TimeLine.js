import React from 'react';
import PropTypes from 'prop-types';
import './TimeTable.css';
import {connect} from 'react-redux'

const ONE_DAY = 24 * 60 * 60;

function TimeInterval(props) {
    let width = 100 * props.duration / ONE_DAY
    let interval_style = {
        backgroundColor: props.color,
        width: `${width}%`,
        height: "20px",
        left: (100 * (props.start_time -  props.initial_time) / ONE_DAY) - props.left_offset + "%"
    }
    return (
        <div className="time-interval" style={interval_style}/>
    )
}

const TimeLine = (props) => {
    let left_offset = 0;
    let intervals = props.intervals.map((interval) => {
        let elem = <TimeInterval key={interval.start + interval.duration}
                                 color="red"
                                 start_time={interval.start}
                                 duration={interval.duration}
                                 initial_time={props.initial_time}
                                 left_offset={left_offset}/>

        // offset by total width of previous intervals
        left_offset += 100 * interval.duration / ONE_DAY
        return elem
    });
    return (
        <tr>
            <td className="text-center">
                {props.ip_addr} <br/> {props.mac_addr}
            </td>
            <td colSpan="24" className="h-100" style={{padding: 0, height: "100%"}}>
                {intervals}
            </td>
        </tr>
    )
}

TimeLine.propTypes = {
    ip_addr: PropTypes.string.isRequired,
    mac_addr: PropTypes.string.isRequired,
    client_id: PropTypes.string.isRequired,
}

TimeInterval.propTypes = {
    color: PropTypes.string.isRequired,
    start_time: PropTypes.number.isRequired,
    duration: PropTypes.number.isRequired,
    initial_time: PropTypes.number.isRequired,
    left_offset: PropTypes.number.isRequired,
}

const mapStateToProps = (state, ownProps) => {
    if (state.monitor.status.hasOwnProperty(ownProps.client_id)) {
        return {intervals: state.monitor.status[ownProps.client_id]}
    } else {
        return {intervals: []}
    }
}

export default connect(mapStateToProps)(TimeLine)
