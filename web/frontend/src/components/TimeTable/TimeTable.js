import React from 'react';
import TimeLine from './TimeLine';
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'

import './TimeTable.css';

let data = {
    "ip_addr": "10.0.0.1",
    "mac_addr": "ff:ff:ff:ff:ff",
    "intervals": [{
        "start": "2021-10-21T03:01:36.014448Z",
        "duration": 5,
    }, {
        "start": "2021-10-21T03:13:36.014448Z",
        "duration": 5,
    }, {
        "start": "2021-10-21T03:05:36.014448Z",
        "duration": 5,
    }, {
        "start": "2021-10-21T03:08:36.014448Z",
        "duration": 5,
    }]
}

function TimeTableHeader(props) {
    let headers = new Array(24);
    headers[0] = "Device"
    for (let i = 1; i <= 11; i++) {
        headers[i] = i + " AM";
        headers[i + 12] = i + " PM";
    }
    headers[11] = "12 PM";

    return (
        <Row className="flex-nowrap text-center">
            {headers.map((x) => {
                return <Col className="border" md='1' key={x}>{x}</Col>
            })}
        </Row>
    )
}

class TimeTable extends React.Component {
    render() {
        return (
            <Container fluid>
                <TimeTableHeader/>
                <TimeLine ip_addr={data.ip_addr}
                          mac_addr={data.mac_addr}
                          intervals={data.intervals}/>
            </Container>
        )
    }
}

export default TimeTable