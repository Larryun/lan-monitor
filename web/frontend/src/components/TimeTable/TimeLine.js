import React from 'react';
import PropTypes from 'prop-types';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import './TimeTable.css';

function TimeInterval(props) {
    let interval_style = {
        backgroundColor: props.color,
        width: 100 * props.duration / (24 * 60)  + "%",
        height: "20px",
        left: 100 * (props.start_time - props.initial_time) / (24 * 60 * 60)  + "%"
    }
    console.log(100 * (props.start_time - props.initial_time) / (24 * 60 * 60))
    return (
        <div className="time-interval" style={interval_style}/>
    )
}

class TimeLine extends React.Component {
    render() {
        let today = new Date()
        let initial_time = new Date(today.getFullYear(), today.getMonth(), today.getDate() - 1)

        let intervals = this.props.intervals.map((interval) => {
            return <TimeInterval key={interval.start}
                                 color="red"
                                 start_time={interval.start}
                                 duration={interval.duration}
                                 initial_time={initial_time.getTime() / 1000}
            />
        });
        return (
            <tr className="align-items-center">
                <td className="text-center">
                    {this.props.ip_addr} <br/> {this.props.mac_addr}
                </td>
                <td colspan="24" className="h-100" style={{padding: 0, height: "100%"}}>
                    {intervals}
                </td>
            </tr>
        )
    }
}

TimeLine.propTypes = {
    ip_addr: PropTypes.string.isRequired,
    mac_addr: PropTypes.string.isRequired,
    intervals: PropTypes.array,
}

TimeInterval.propTypes = {
    color: PropTypes.string.isRequired,
    start_time: PropTypes.number.isRequired,
    duration: PropTypes.number.isRequired,
}

export default TimeLine