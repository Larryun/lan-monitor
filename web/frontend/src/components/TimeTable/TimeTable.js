import React from 'react';
import TimeLine from './TimeLine';
import Container from 'react-bootstrap/Container'
import Table from 'react-bootstrap/Table'

import {getClients} from '../../api/monitor'

import './TimeTable.css';

function TimeTableHeader() {
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
        let today = new Date()
        // get date only
        let initial_time = new Date(today.getFullYear(), today.getMonth(), today.getDate())

        return (
            <Container fluid style={{width: "max-content", padding: 0}}>
                <Table>
                    <TimeTableHeader/>
                    <tbody>
                    {this.state.clients.map((c) => {
                        return <TimeLine key={c.mac_addr}
                                         ip_addr={c.ip_addr}
                                         mac_addr={c.mac_addr}
                                         client_id={c._id}
                                         initial_time={initial_time.getTime()}
                        />
                    })}
                    </tbody>
                </Table>
            </Container>
        )
    }
}

export default TimeTable