import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import App from './components/App';
import Home from './components/Home';
import About from './components/About';
import Contacts from './components/Contacts';
import Shop from './components/Shop';

import links from './links.json';
import geti18n from './i18n';
import Product from './components/Product';
import Cart from './components/Cart';

geti18n()

const root = createRoot(
	document.getElementById('main') as HTMLElement
);

export interface LinkFilters {
	key: string,
	multiple: boolean,
	values: string[]
}

export interface Link {
	name: string,
	image: string,
	count: number,
	filters: LinkFilters[]
}

export interface LinksProps {
	links: Link[]
}

root.render(
	<React.StrictMode>
		<BrowserRouter>
			<Routes>
				<Route path='' element={<App />}>
					<Route path='/' element={<Home links={links} />} />
					<Route path='/shop/:category/' element={<Shop links={links} />} />
					<Route path='/product/:category/:name/' element={<Product />} />
					<Route path='/cart/' element={<Cart />} />
					<Route path='/about/' element={<About />} />
					<Route path='/contacts/' element={<Contacts />} />
				</Route>
			</Routes>
		</BrowserRouter>
	</React.StrictMode>
);
