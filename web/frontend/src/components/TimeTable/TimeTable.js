import React from 'react';
import TimeLine from './TimeLine';
import Container from 'react-bootstrap/Container'
import Table from 'react-bootstrap/Table'

import {getClients} from '../../api/monitor'

import './TimeTable.css';

let data = {
    "ip_addr": "10.0.0.1",
    "mac_addr": "ff:ff:ff:ff:ff",
    "intervals": [{
        "start": 1640832987.9042091,
        "duration": 5,
    }, {
        "start": 1640832937.1988218,
        "duration": 5,
    }, {
        "start": 1640832886.5146236,
        "duration": 5,
    }, {
        "start": 1640842790.7178771,
        "duration": 60,
    }]
}

function TimeTableHeader(props) {
    let headers = new Array(24);
    headers[0] = "Device"
    for (let i = 0; i < 24; i++) {
        headers[i + 1] = i + ":00"
    }

    return (
        <thead className="text-center">
        <tr>
            {headers.map((x) => {
                return <th className="border" key={x}>{x}</th>
            })}
        </tr>
        </thead>
    )
}

class TimeTable extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            clients: [],
        }
    }

    componentDidMount() {
        getClients().then((res) => {
            this.setState({
                clients: res.data
            })
        })
    }

    render() {
        return (
            <Container fluid style={{width: "max-content", padding: 0}}>
                <Table>
                    <TimeTableHeader/>
                    <TimeLine ip_addr={data.ip_addr}
                              mac_addr={data.mac_addr}
                              intervals={data.intervals}/>
                </Table>
            </Container>
        )
    }
}

export default TimeTable