import React from 'react';
import TimeLine from './TimeLine';
import Container from 'react-bootstrap/Container'

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

class TimeTable extends React.Component {
    render() {
        return (
            <Container>
                <TimeLine ip_addr={data.ip_addr}
                          mac_addr={data.mac_addr}
                          intervals={data.intervals}/>
            </Container>
        )
    }
}

export default TimeTable