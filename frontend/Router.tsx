import { Router, Routes, Route } from '@solidjs/router';
import { lazy } from 'solid-js';
import App from './App';
import Navigation from './components/Navigation';

const TransactionsPage = lazy(() => import('./Transactions'));

export default function AppRouter() {
    return (
        <>
            <Router>
                <Navigation />
                <Routes>
                    <Route path="/" component={App} />
                    <Route path="/transactions" component={TransactionsPage} />
                </Routes>
            </Router>
        </>
    );
}

