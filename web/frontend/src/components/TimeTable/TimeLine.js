import React from 'react';
import PropTypes from 'prop-types';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import './TimeTable.css';

function TimeInterval(props) {
    let interval_style = {
        'background-color': props.color,
        width: props.width + '%',
    }
    return (
        <div className="time-interval" style={interval_style}>
            {Date.parse(props.start_time)}
        </div>
    )
}

class TimeLine extends React.Component {

    render() {
        let intervals = this.props.intervals.map((interval) => {
            return <TimeInterval color="red" start_time={interval.start} duration={interval.duration}/>
        });
        return (
            <Row className="align-items-center">
                <Col md="1" xs={5}>
                    <Row>{this.props.ip_addr}</Row>
                    <Row>{this.props.mac_addr}</Row>
                </Col>
                <Col style={{padding: 0}}>
                    {intervals}
                </Col>
            </Row>
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
    start_time: PropTypes.string.isRequired,
    duration: PropTypes.number.isRequired,
}

export default TimeLine