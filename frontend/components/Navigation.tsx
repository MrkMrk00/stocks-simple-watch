import { ParentProps } from "solid-js";
import { A } from "@solidjs/router";

function NavLink(props: ParentProps<{ href: string; class?: string }>) {
    const { href, children, class: className } = props;

    return (
        <A href={href} class={'p-4 bg-white hover:brightness-95 ' + className || ''}>
            { children }
        </A>
    );
}


export default function Navigation() {
    return (
        <nav class="">
            <div class="flex flex-row px-4 bg-white shadow-md">
                <NavLink href="/" class="border-l">Homepage</NavLink>
                <NavLink href="/transactions" class="border-x">Transactions</NavLink>
            </div>
        </nav>
    );
}
