import React from 'react';
import PropTypes from 'prop-types';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';

class TimeLine extends React.Component {
    render() {
        return (
            <Row className="align-items-center">
                <Col md="2" xs={5}>
                    <Row>{this.props.ip_addr}</Row>
                    <Row>{this.props.mac_addr}</Row>
                </Col>
                <Col>
                    <span>hi</span>
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

export default TimeLine