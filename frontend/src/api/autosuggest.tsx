type ApiSuccessResponse<T> = {
    data: T;
    error: null;
};

type ApiErrorResponse<T> = {
    data: null;
    error: T;
};

type ApiResponse<T, E> = ApiSuccessResponse<T> | ApiErrorResponse<E>;

const useAutoSuggest = () => {

    const getAutoSuggest = async (query: string): Promise<ApiResponse<string, string>> => {
        try {
            const response = await fetch(
                `${import.meta.env.VITE_API_URL}/autosuggest?query=${query}`,
                {
                    method: "GET",
                    mode: "cors",
                }
            );

            const jsonResponse = await response.json();

            if (jsonResponse.error) {
                return { data: null, error: jsonResponse.message };
            }

            return { data: jsonResponse.message, error: null };

            // eslint-disable-next-line @typescript-eslint/no-unused-vars
        } catch (error) { // error caught not used
            return { data: null, error: 'Network error' };
        }
    };

    return {
        getAutoSuggest
    };
};

export default useAutoSuggest;