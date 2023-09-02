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

export interface ResponsiveProps {
	isMobile: boolean
}

const isMobile = window.matchMedia('(max-width: 1080px)').matches

root.render(
	<React.StrictMode>
		<BrowserRouter>
			<Routes>
				<Route path='' element={<App isMobile={isMobile} />}>
					<Route path='/' element={<Home isMobile={isMobile} links={links} />} />
					<Route path='/shop/:category/' element={<Shop isMobile={isMobile} links={links} />} />
					<Route path='/product/:category/:name/' element={<Product isMobile={isMobile} />} />
					<Route path='/cart/' element={<Cart isMobile={isMobile} />} />
					<Route path='/about/' element={<About isMobile={isMobile} />} />
					<Route path='/contacts/' element={<Contacts isMobile={isMobile} />} />
				</Route>
			</Routes>
		</BrowserRouter>
	</React.StrictMode>
);
