import { ParentProps } from "solid-js";
import { A } from "@solidjs/router";

function NavLink(props: ParentProps<{ href: string }>) {
    const { href, children } = props;

    return (
        <A href={href}>
            { children }
        </A>
    );
}


export default function Navigation() {
    return (
        <nav class="">
            <div class="flex flex-row gap-3">
                <NavLink href="/">Homepage</NavLink>
                <NavLink href="/transactions">Transactions</NavLink>
            </div>
        </nav>
    );
}
