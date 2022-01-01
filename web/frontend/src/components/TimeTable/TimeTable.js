import React from 'react';
import TimeLine from './TimeLine';
import Container from 'react-bootstrap/Container'
import Table from 'react-bootstrap/Table'
import DatePicker from 'react-datepicker';

import {getDateOnly} from "../../util";
import {getClients} from '../../api/monitor'

import './TimeTable.css';
import "react-datepicker/dist/react-datepicker.css";


function TimeTableHeader() {
    let headers = new Array(24);
    headers[0] = "Device"
    for (let i = 0; i < 24; i++) {
        headers[i + 1] = i + ":00"
    }

    return (
        <thead className="text-center">
            <tr className="time-table-header">
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
            initial_time: getDateOnly(new Date())
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
                <DatePicker selected={this.state.initial_time} onChange={(date) => {
                    this.setState({initial_time: getDateOnly(date)})
                }}/>
                <Table bordered={true}>
                    <TimeTableHeader/>
                    <tbody>
                    {this.state.clients.map((c) => {
                        return <TimeLine key={c.mac_addr}
                                         ip_addr={c.ip_addr}
                                         mac_addr={c.mac_addr}
                                         client_id={c._id}
                                         initial_time={this.state.initial_time.getTime() / 1000}
                        />
                    })}
                    </tbody>
                </Table>
            </Container>
        )
    }
}

export default TimeTable