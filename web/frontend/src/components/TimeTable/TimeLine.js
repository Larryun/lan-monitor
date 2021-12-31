import React from 'react';
import PropTypes from 'prop-types';
import './TimeTable.css';
import {getClientStatus} from '../../api/monitor'

const ONE_DAY = 24 * 60 * 60;

function TimeInterval(props) {
    let interval_style = {
        backgroundColor: props.color,
        width: 100 * props.duration / ONE_DAY + "%",
        height: "20px",
        left: (100 * (props.start_time - props.initial_time) / ONE_DAY) - props.left_offset + "%"
    }
    return (
        <div className="time-interval" style={interval_style}/>
    )
}

class TimeLine extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            intervals: []
        }
    }

    componentDidMount() {
        let one_day = 24 * 60 * 60;
        getClientStatus(
            this.props.client_id,
            this.props.initial_time / 1000,
            (this.props.initial_time / 1000) + one_day,
            100
        ).then((res) => {
            this.setState({
                intervals: res.data
            })
        })
    }

    render() {
        let left_offset = 0;
        let intervals = this.state.intervals.map((interval) => {
            let elem = <TimeInterval key={interval.start + interval.duration}
                                     color="red"
                                     start_time={interval.start}
                                     duration={interval.duration}
                                     initial_time={this.props.initial_time / 1000}
                                     left_offset={left_offset}/>

            // offset by total width of previous intervals
            left_offset += 100 * interval.duration / ONE_DAY
            return elem
        });
        return (
            <tr className="align-items-center">
                <td className="text-center">
                    {this.props.ip_addr} <br/> {this.props.mac_addr}
                </td>
                <td colSpan="24" className="h-100" style={{padding: 0, height: "100%"}}>
                    {intervals}
                </td>
            </tr>
        )
    }
}

TimeLine.propTypes = {
    ip_addr: PropTypes.string.isRequired,
    mac_addr: PropTypes.string.isRequired,
    client_id: PropTypes.string.isRequired,
    initial_time: PropTypes.number.isRequired,
}

TimeInterval.propTypes = {
    color: PropTypes.string.isRequired,
    start_time: PropTypes.number.isRequired,
    duration: PropTypes.number.isRequired,
    initial_time: PropTypes.number.isRequired,
    left_offset: PropTypes.number.isRequired,
}

export default TimeLine