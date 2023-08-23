import React, { useCallback } from 'react'
import Menu from './Menu';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAngleUp } from '@fortawesome/free-solid-svg-icons';
import Footer from './Footer';
import { Outlet } from 'react-router-dom';
import useCart from './_hooks/useCart';
import { Product, Size } from '../JSONTypes';

export interface OutletContextProps {
	products: Product[],
	total: number,
	count: number,
	addSize: (product: Product) => void,
	deleteSize: (product: Product) => void,
	updateQuantity: (product: Product, size: Size, value: number) => void
	clearProduct: (product: Product, size: Size) => Product
}

export default function App() {
	const { products, total, count, addSize, deleteSize, updateQuantity, clearProduct } = useCart()

	return (
		<div className='d-flex flex-column'>
			<Menu count={count}/>
			<Outlet context={{
				products: products,
				total: total,
				count: count,
				addSize: addSize,
				deleteSize: deleteSize,
				updateQuantity: updateQuantity,
				clearProduct: clearProduct
			}}/>
			<Footer />
			<div
				id='scroll_to_top_button'
				onClick={() => window.scrollTo({top: 0, behavior: 'smooth'})}
				style={{width: '3vw', aspectRatio: 1, bottom: '3vw', left: '3vw', opacity: 0}}
				className='d-flex position-fixed transition-l bg-blue rounded-circle justify-content-center align-items-center h4'>
				<FontAwesomeIcon icon={faAngleUp} />
			</div>
		</div>
	);
}
