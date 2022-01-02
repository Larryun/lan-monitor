import React from 'react'
import TimeLine from './TimeLine'
import Container from 'react-bootstrap/Container'
import Table from 'react-bootstrap/Table'
import DatePicker from 'react-datepicker'
import Row from 'react-bootstrap/row'
import Col from 'react-bootstrap/col'
import Button from 'react-bootstrap/button'
import store from '../../store'
import {connect} from 'react-redux'

import './TimeTable.css';
import "react-datepicker/dist/react-datepicker.css";
import {decrementCurrentDate, fetchClients, incrementCurrentDate, setDateAndFetchStatus} from "../../actions";


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
    componentDidMount() {
        store.dispatch(fetchClients())
    }

    render() {
        return (
            <Container fluid style={{width: "max-content", padding: 0}}>
                <div className="d-flex flex-row justify-content-center">
                    <Button onClick={() => store.dispatch(decrementCurrentDate())}>Previous Day</Button>
                    <DatePicker className="time-table-datepicker" selected={this.props.current_date * 1000} onChange={(date) => {
                        store.dispatch(setDateAndFetchStatus(date.getTime() / 1000))
                    }}/>
                    <Button onClick={() => store.dispatch(incrementCurrentDate())}>Next Day</Button>
                </div>
                <Table bordered={true}>
                    <TimeTableHeader/>
                    <tbody>
                    {this.props.clients.map((c) => {
                        return <TimeLine key={c.mac_addr}
                                         ip_addr={c.ip_addr}
                                         mac_addr={c.mac_addr}
                                         client_id={c._id}
                                         initial_time={this.props.current_date}
                        />
                    })}
                    </tbody>
                </Table>
            </Container>
        )
    }
}

const mapStateToProps = (state) => ({
    clients: state.monitor.clients,
    current_date: state.monitor.current_date
})


export default connect(mapStateToProps)(TimeTable)