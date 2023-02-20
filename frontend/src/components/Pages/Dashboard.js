import React, { Component } from 'react'
import  { Navigate } from 'react-router-dom'


export default class Dashboard extends Component {
    render() {
        if(!localStorage.getItem('token')){
            return <Navigate to='login'/>
        }
        return (
            <div>
                {localStorage.getItem('user')}
            </div>
        )
    }
}